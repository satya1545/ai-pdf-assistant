from utils.vector_store import collection
from utils.embedding import model


def search_documents(query: str, top_k=3):

    query_embedding = model.encode([query])

    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=top_k
    )

    return results