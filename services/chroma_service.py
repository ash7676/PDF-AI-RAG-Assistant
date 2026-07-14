import chromadb

client =  chromadb.PersistentClient(path="./data")
collection = client.get_or_create_collection(name="employee_handbook")


def add_document(id,chunk,embedding):
    collection.add(
        ids=[id],
        documents=[chunk],
        embeddings=[embedding]
    )
    
def reset_collection():
    global collection
    client.delete_collection(name="employee_handbook")
    collection = client.get_or_create_collection(
        name="employee_handbook"
    )
    