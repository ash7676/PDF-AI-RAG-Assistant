import logging
from fastapi import Request
from fastapi.responses import JSONResponse

from exceptions.exceptions import (EmbeddingGenerationException,PDFReadError,VectorSearchError,LLMResponseError,ChromaDBError)
logger = logging.getLogger(__name__)

async def embedding_generation_exception_handler(
    request:Request,exc:EmbeddingGenerationException
):
    logger.error("Embedding Generation Failed!")
    return JSONResponse(
        status_code=500,
        content={
            "error":"unable to generate embeddings."
        }
    )

async def pdf_read_exception_handler(request:Request,exc:PDFReadError):
    logger.error("PDF reading failed!")
    return JSONResponse(
        status_code=500,
        content={
            "error":"Unable to read the PDF"
        }
    )

async def vector_search_exception_handler(request: Request,exc:VectorSearchError):
    logger.error("vector search failed!")
    return JSONResponse(status_code=500,content={"error":"unable to search the document"})

async def llm_reponse_exception_handler(
    request:Request,
    exc:LLMResponseError
):
    logger.error("LLM Response Generation Failed!")
    return JSONResponse(
        stauts_code=500,
        content={
            "error":"unable generate and answer"
        }
    )

async def chroma_db_exception_handler(
    request:Request,
    exc:ChromaDBError
):
    logger.error("chroma DB Operation Failed")
    return JSONResponse(
        status_code=500,
        content={
            "erorr":"vector database error"
        }
    )