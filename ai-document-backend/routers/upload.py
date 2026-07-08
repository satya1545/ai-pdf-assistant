import os
from fastapi import APIRouter, UploadFile, File, HTTPException
from utils.pdf_reader import extract_text_from_pdf
from utils.text_splitter import chunk_text
from fastapi import Depends
from sqlalchemy.orm import Session

from database.db import get_db
from services.document_service import create_document
from utils.dependencies import get_current_user
import uuid
import os

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
    current_user = Depends(get_current_user)
):

    # Check file type
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    file_extension = os.path.splitext(file.filename)[1]

    unique_filename = f"{uuid.uuid4()}{file_extension}"

    file_path = os.path.join("uploads", unique_filename)
    

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    text = extract_text_from_pdf(file_path)

    logger.info()

    logger.warning()

    logger.error()

    chunks = chunk_text(text)

    logger.info()

    logger.warning()

    logger.error()
    from utils.embedding import create_embeddings
    from utils.vector_store import store_embeddings

    embeddings = create_embeddings(chunks)

    logger.info()

    logger.warning()

    logger.error()

    document = create_document(
    db=db,
    original_filename=file.filename,
    stored_filename=unique_filename,
    filepath=file_path,
    total_chunks=len(chunks),
    user_id=current_user.id
)
    return {
    "message": "Uploaded Successfully",
    "document_id": document.id,
    "filename": document.filename,
    "chunks": document.total_chunks,
    "filename": file.filename,
    "chunks": len(chunks),
    # "vectors_stored": count,
    "total_characters": len(text),
    "total_chunks": len(chunks),
    "first_chunk": chunks[0]
}
# }
#     return {
#     "filename": file.filename,
#     "total_characters": len(text),
#     "total_chunks": len(chunks),
#     "first_chunk": chunks[0]
# }