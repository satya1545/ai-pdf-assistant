import os
import uuid

from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session

from database.db import get_db
from utils.dependencies import get_current_user

from utils.pdf_reader import extract_text_from_pdf
from utils.text_splitter import chunk_text
from utils.embedding import create_embeddings
from utils.vector_store import store_embeddings

from services.document_service import create_document

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/pdf")
async def upload_pdf(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    extension = os.path.splitext(file.filename)[1]
    unique_filename = f"{uuid.uuid4()}{extension}"

    file_path = os.path.join(
        UPLOAD_FOLDER,
        unique_filename
    )

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    text = extract_text_from_pdf(file_path)

    print("TEXT LENGTH:", len(text))

    chunks = chunk_text(text)

    print("TOTAL CHUNKS:", len(chunks))

    if len(chunks) == 0:
        raise HTTPException(
            status_code=400,
            detail="No text found inside PDF."
        )

    embeddings = create_embeddings(chunks)

    print("EMBEDDINGS:", len(embeddings))

    vectors_stored = store_embeddings(
        chunks,
        embeddings
    )

    document = create_document(
        db=db,
        filename=file.filename,
        filepath=file_path,
        total_chunks=len(chunks),
        user_id=current_user.id
    )

    return {
        "message": "Uploaded Successfully",
        "document_id": document.id,
        "filename": document.filename,
        "vectors_stored": vectors_stored,
        "total_characters": len(text),
        "total_chunks": len(chunks)
    }