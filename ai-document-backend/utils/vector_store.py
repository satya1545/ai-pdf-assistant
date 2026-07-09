import chromadb
import uuid

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="documents"
)


def store_embeddings(chunks, embeddings):

    print("Chunks:", len(chunks))
    print("Embeddings:", len(embeddings))

    ids = [str(uuid.uuid4()) for _ in range(len(chunks))]

    print("IDs:", len(ids))

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist()
    )

    print("Total vectors:", collection.count())

    return collection.count()