from services.pdf_service import get_pdf_text
from services.chunker import split_into_chunks
from services.embedding_service import generate_embedding
from services.storage_service import load_documents,save_documents

documents = load_documents()
if documents is None:
    documents = []
    print("No saved embeddings found.")
    print("Generating embeddings...")
    text =  get_pdf_text()
    chunks = split_into_chunks(text)

    # documents =[]
    for index,chunk in enumerate(chunks):
        print(f"generating embedding for the chunk {index+1}/{len(chunks)}")
        embedding = generate_embedding(chunk)
        documents.append({
            "chunk":chunk,
            "embedding": embedding
        })
    save_documents(documents)
else:
    print("loaded embeddings from disk")
    
print("total chunks:",len(documents))
print()
print("first chunk:")

print(documents[0]["chunk"])

print()

print("embedding length:")
print(len(documents[0]["embedding"]))
