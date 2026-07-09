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

    print("=" * 80)
    print(results)
    print("=" * 80)

    documents = results["documents"][0]

    print("Retrieved Chunks:")
    for i, doc in enumerate(documents):
        print(f"\nChunk {i+1}:")
        print(doc[:300])

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