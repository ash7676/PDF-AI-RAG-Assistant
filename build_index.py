from services.pdf_service import get_pdf_text
from services.chunker import split_into_chunks
from services.embedding_service import generate_embedding
from services.chroma_service import add_document,reset_collection
import config.logging_config
import logging

logger =  logging.getLogger(__name__)
text =  get_pdf_text()

chunks = split_into_chunks(text)

reset_collection()

for index,chunk in enumerate(chunks):
    logger.info(f"generating embedding for the chunk {index+1}/{len(chunks)}")
    embedding = generate_embedding(chunk)
    add_document(
        id=f"chunk_{index}",
        chunk=chunk,
        embedding=embedding
    )