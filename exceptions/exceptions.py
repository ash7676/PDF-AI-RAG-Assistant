class RAGException(Exception):
    """Base Exception for the application."""

class EmbeddingGenerationException(RAGException):
    """Raised when embedding generation fails."""

class PDFReadError(RAGException):
    """Raised when there is error in reading the pdf"""

class VectorSearchError(RAGException):
    """Raised when there is error in vector search"""

class LLMResponseError(RAGException):
    """Raised when there is error in LLM Response."""
    
class ChromaDBError(RAGException):
    """Raised when there is error in Chroma db"""