import logging
logger = logging.getLogger(__name__)
def split_into_chunks(text,chunk_size=500):
    logger.info("Splitting document into chunks...")
    chunks=[]
    for i in range(0, len(text),chunk_size):
        chunks.append(text[i:i+chunk_size])
    logger.info("total chunks : {len(chunks)}")
    return chunks