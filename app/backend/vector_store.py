from langchain_community.vectorstores import FAISS

from backend.config import VECTOR_STORE_SEARCH_K, VECTOR_STORE_SEARCH_TYPE


def create_vector_store(docs, embeddings):
    try: 
        vector_store = FAISS.from_documents(docs, embeddings)
        return vector_store
    except Exception as e:
        raise ValueError(f"Error creating vector store: {e}")

def get_retriever(vector_store):
    retriever = vector_store.as_retriever(search_type= VECTOR_STORE_SEARCH_TYPE , search_kwargs={"k": VECTOR_STORE_SEARCH_K})
    return retriever