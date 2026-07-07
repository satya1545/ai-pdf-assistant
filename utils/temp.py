from utils.embedding import create_embeddings

chunks = [
    "Python is a programming language.",
    "FastAPI is a backend framework.",
    "Cats are animals."
]

embeddings = create_embeddings(chunks)

print(len(embeddings))
print(len(embeddings[0]))