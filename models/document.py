from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func

from database.db import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String, nullable=False)

    filepath = Column(String, nullable=False)

    total_chunks = Column(Integer)

    uploaded_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )