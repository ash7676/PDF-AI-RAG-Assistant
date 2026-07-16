import chromadb
from config.settings import CHROMA_COLLECTION,CHROMA_DB_PATH
import logging

logger = logging.getLogger(__name__)
client =  chromadb.PersistentClient(path=CHROMA_DB_PATH)
collection = client.get_or_create_collection(name=CHROMA_COLLECTION)


def add_document(id,chunk,embedding):
    collection.add(
        ids=[id],
        documents=[chunk],
        embeddings=[embedding]
    )
    
def reset_collection():
    logger.info("Resetting chroma collection...")
    global collection
    client.delete_collection(name=CHROMA_COLLECTION)
    collection = client.get_or_create_collection(
        name=CHROMA_COLLECTION
    )
    