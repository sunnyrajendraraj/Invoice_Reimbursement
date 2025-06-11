import chromadb

# Use the new ChromaDB PersistentClient API (as per migration guide)
client = chromadb.PersistentClient(path=".chromadb")
collection = client.get_or_create_collection(name="invoice_analysis")

def store_embedding(text: str, metadata: dict):
    """
    Store embedding and metadata in vector store.
    """
    from app.core.embeddings import get_embedding
    embedding = get_embedding(text)
    collection.add(
        documents=[text],
        metadatas=[metadata],
        embeddings=[embedding]
    )

def similarity_search(query: str, filters: dict = None, k: int = 5):
    """
    Perform similarity search with optional metadata filters.
    Returns list of matching documents with metadata.
    """
    from app.core.embeddings import get_embedding
    query_embedding = get_embedding(query)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k,
        where=filters or {}
    )
    return [
        {"document": doc, "metadata": meta}
        for doc, meta in zip(results['documents'][0], results['metadatas'][0])
    ]
