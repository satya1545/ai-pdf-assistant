import os

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.db import get_db
from models.document import Document
from schemas.document import DocumentResponse
from utils.dependencies import get_current_user

from services.document_service import (
    get_document_by_id,
    delete_document
)

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.get(
    "/",
    response_model=list[DocumentResponse]
)
def get_documents(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    documents = (
        db.query(Document)
        .filter(Document.user_id == current_user.id)
        .all()
    )

    return documents


@router.delete("/{document_id}")
def delete_document_route(
    document_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    document = get_document_by_id(
        db,
        document_id,
        current_user.id
    )

    if not document:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    if os.path.exists(document.filepath):
        os.remove(document.filepath)

    delete_document(
        db,
        document
    )

    return {
        "message": "Document deleted successfully"
    }