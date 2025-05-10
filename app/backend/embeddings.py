from langchain_google_genai import GoogleGenerativeAIEmbeddings

from backend.config import GOOGLE_API_KEY


def get_embedding_model():
    return GoogleGenerativeAIEmbeddings(model="models/text-embedding-004", google_api_key=GOOGLE_API_KEY)