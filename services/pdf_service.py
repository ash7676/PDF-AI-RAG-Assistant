from pypdf import PdfReader
from config.settings import PDF_PATH
import config.logging_config
import logging
from exceptions.exceptions import PDFReadError
logger =  logging.getLogger(__name__)
def get_pdf_text():
    try:
        logger.info('Reading PDF....')
        reader = PdfReader(PDF_PATH)
        text=""
        for page in reader.pages:
            page_text = page.extract_text() 
            if page_text:
                text+= page_text + "\n"
        return text 
    except Exception as e:
        raise PDFReadError() from e