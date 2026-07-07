import chromadb

client = chromadb.Client()

collection = client.get_or_create_collection(
    name="documents"
)


def store_embeddings(chunks, embeddings):

    ids = [str(i) for i in range(len(chunks))]

    collection.add(
        documents=chunks,
        embeddings=embeddings.tolist(),
        ids=ids
    )

    return collection.count()
print("Total vectors:", collection.count())