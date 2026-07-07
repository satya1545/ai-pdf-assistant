from fastapi import APIRouter

from utils.search import search_documents
from services.gemini_service import generate_answer

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.get("/")
def chat(question: str):

    results = search_documents(question)

    documents = results["documents"][0]

    context = "\n\n".join(documents)

    answer = generate_answer(
        context,
        question
    )

    return {
        "question": question,
        "answer": answer,
        "sources": documents
    }