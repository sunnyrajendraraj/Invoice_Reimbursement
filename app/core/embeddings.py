from sentence_transformers import SentenceTransformer

# Load embedding model once
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text: str):
    """
    Generate vector embedding for given text.
    """
    return embedding_model.encode(text).tolist()
