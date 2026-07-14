from services.pdf_service import get_pdf_text
from services.chunker import split_into_chunks
from services.embedding_service import generate_embedding
from services.chroma_service import add_document,reset_collection

print("reading PDF...")
text =  get_pdf_text()

print("splitting document into chunks...")
chunks = split_into_chunks(text)
print(f"total chunks: {len(chunks)}")

print("resetting chroma collection...")
reset_collection()

for index,chunk in enumerate(chunks):
    print(f"generating embedding for the chunk {index+1}/{len(chunks)}")
    embedding = generate_embedding(chunk)
    add_document(
        id=f"chunk_{index}",
        chunk=chunk,
        embedding=embedding
    )