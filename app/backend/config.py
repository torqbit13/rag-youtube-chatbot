import os

from dotenv import load_dotenv

load_dotenv()
# Google api key for querying to google's LLMs
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# File path of chat history
CHAT_HISTORY_FILE = "chat_history.txt"

# Model Configuration
EMBEDDING_MODEL_NAME = "models/text-embedding-004"
LLM_MODEL_NAME = "gemini-1.5-flash"

# Text Splitting Configuration
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Vector Store Configuration
VECTOR_STORE_SEARCH_TYPE = "similarity"
VECTOR_STORE_SEARCH_K = 4
