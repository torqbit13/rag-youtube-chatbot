import streamlit as st
from backend.chain import build_chain
from backend.embeddings import get_embedding_model
from backend.ingestion import fetch_transcript
from backend.splitter import split_transcript
from backend.vector_store import create_vector_store, get_retriever

st.title("📽️ RAG-Based YouTube Transcript Chatbot")

video_url = st.text_input("Paste a YouTube Video URL:")
question = st.text_input("Ask a question based on the video:")

if video_url:
    try:
        video_id = video_url.split("v=")[-1].split("&")[0]
        transcript = fetch_transcript(video_id)
        st.success("Transcript fetched successfully!")

        docs = split_transcript(transcript)
        embeddings = get_embedding_model()
        vector_store = create_vector_store(docs, embeddings)
        retriever = get_retriever(vector_store)
        chain = build_chain(retriever)

        if question:
            response = chain.invoke(question)
            st.markdown("### 🧠 Answer:")
            st.write(response)

    except Exception as e:
        st.error(str(e))
