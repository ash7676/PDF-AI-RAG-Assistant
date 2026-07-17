import ollama
from config.settings import EMBEDDING_MODEL
import logging
from exceptions.exceptions import EmbeddingGenerationException
logger =  logging.getLogger(__name__)
MODEL = EMBEDDING_MODEL

def generate_embedding(text:str) ->list[float]:
    try:
        response = ollama.embed(
            model=MODEL,
            input=text
        )
        print("response---",response)
        return response["embeddings"][0]
    except Exception as e:
        logger.exception(f"embedding generation failed using mode: {MODEL}")
        raise EmbeddingGenerationException() from e