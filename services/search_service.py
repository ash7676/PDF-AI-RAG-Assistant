from services.embedding_service import generate_embedding
# from services.similarity_service import cosine_similarity
from services.chroma_service import collection

# def search(question,documents,top_k=3):
#     question_embedding =  generate_embedding(question)
#     results = []
#     for document in documents:
#         score = cosine_similarity(question_embedding,document["embedding"])
#         results.append({"score":score,
#                         "chunk":document["chunk"]})
#     results.sort(
#         key=lambda result:result["score"],
#         reverse= True
#     )
#     return results[:top_k]
def search(question,top_k=3):
    question_embedding =  generate_embedding(question)
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=top_k
    )
    return results["documents"][0]