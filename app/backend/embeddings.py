from langchain_google_genai import GoogleGenerativeAIEmbeddings

from backend.config import GOOGLE_API_KEY, EMBEDDING_MODEL_NAME


def get_embedding_model():
    embeddings = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL_NAME, google_api_key=GOOGLE_API_KEY
    )
    return embeddings
