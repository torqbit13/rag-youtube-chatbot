from langchain_community.vectorstores import FAISS


def create_vector_store(docs, embeddings):
    return FAISS.from_documents(docs, embeddings)

def get_retriever(vector_store, k=4):
    return vector_store.as_retriever(search_type="similarity", search_kwargs={"k": k})