from pypdf import PdfReader
from config.settings import PDF_PATH

def get_pdf_text():
    reader = PdfReader(PDF_PATH)
    text=""
    for page in reader.pages:
        page_text = page.extract_text() 
        if page_text:
            text+= page_text + "\n"
    return text