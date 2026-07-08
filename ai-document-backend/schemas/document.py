from pydantic import BaseModel
from datetime import datetime


class DocumentResponse(BaseModel):
    id: int
    filename: str
    total_chunks: int
    uploaded_at: datetime

    class Config:
        from_attributes = True