import json
import os

def save_documents(documents,filename="data/embeddings.json"):
    with open(filename,"w") as file:
        json.dump(documents,file)
    print("documents saved successfully..!")
    
def load_documents(filename="data/embeddings.json"):
    if not os.path.exists(filename):
        return None
    
    with open(filename,"r") as file:
        documents =  json.load(file)
    
    print("documents loaded successfully..")
    return documents