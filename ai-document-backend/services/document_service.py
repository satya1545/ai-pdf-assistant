from sqlalchemy.orm import Session

from models.document import Document


def create_document(
    db: Session,
    filename: str,
    filepath: str,
    total_chunks: int,
    user_id: int
):

    document = Document(
        filename=filename,
        filepath=filepath,
        total_chunks=total_chunks,
        user_id=user_id
    )

    db.add(document)

    db.commit()

    db.refresh(document)

    return document