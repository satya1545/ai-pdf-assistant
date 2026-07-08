from fastapi import FastAPI

from database.db import Base, engine

from models.user import User

from routers.upload import router as upload_router

from routers.auth import router as auth_router

from routers.user import router as user_router

from routers.chat import router as chat_router

from models.document import Document

from routers.document import router as document_router

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="AI Backend API"
)

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)

app.include_router(user_router)

app.include_router(upload_router)

app.include_router(chat_router)

app.include_router(document_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "AI Backend API Running"
    }