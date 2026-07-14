import chromadb
from services.embedding_service import generate_embedding
client =  chromadb.PersistentClient(path="./data")
collection = client.get_or_create_collection(name="employee_handbook")
print("collection created successfully!!")
chunk ="employees receive 20 casual leaves"
embedding = generate_embedding(chunk)
collection.add(ids=["chunk_1"],documents=[chunk],embeddings=[embedding])
print("document added successfully.")
question = "how many casual leaves do employees get?"
question_embedding = generate_embedding(question)
results = collection.query(
    query_embeddings=[question_embedding],
    n_results=1
)
print("documents---",results['documents'])
chunks =  results["documents"][0]
# prompt =  "\n\n".join(results)
prompt = "\n\n".join(chunks)
print("prompt----",prompt)