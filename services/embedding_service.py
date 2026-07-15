import ollama
from config.settings import EMBEDDING_MODEL
MODEL = EMBEDDING_MODEL

def generate_embedding(text):
    response = ollama.embed(
        model=MODEL,
        input=text
    )
    return response["embeddings"][0]