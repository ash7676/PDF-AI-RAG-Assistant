from dotenv import load_dotenv
import os

load_dotenv()
CHAT_MODEL = os.getenv("CHAT_MODEL")
OLLAMA_URL = os.getenv("OLLAMA_URL")
EMBEDDING_MODEL = os.getenv('EMBEDDING_MODEL')
CHROMA_COLLECTION = os.getenv("CHROMA_COLLECTION")
CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH")
PDF_PATH = os.getenv("PDF_PATH")