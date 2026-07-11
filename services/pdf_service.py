from pypdf import PdfReader
def get_pdf_text():
    reader = PdfReader("documents/employee-handbook.pdf")
    text=""
    for page in reader.pages:
        page_text = page.extract_text() 
        if page_text:
            text+= page_text + "\n"
    return text