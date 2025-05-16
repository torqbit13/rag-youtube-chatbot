import streamlit as st
from backend.chain import build_chain
from loguru import logger
from backend.config import GOOGLE_API_KEY
from backend.embeddings import get_embedding_model
from backend.history import clear_chat_history, load_chat_history, save_chat_history
from backend.ingestion import fetch_transcript
from backend.splitter import split_transcript
from backend.vector_store import create_vector_store, get_retriever
from langchain_core.messages import AIMessage, HumanMessage


def render_chat():
    history = load_chat_history()
    for msg in history:
        if isinstance(msg, HumanMessage):
            with st.chat_message("user"):
                st.markdown(msg.content)
        elif isinstance(msg, AIMessage):
            with st.chat_message("assistant"):
                st.markdown(msg.content)


def main():
    st.set_page_config(page_title="Conversational RAG YouTube Chatbot")
    st.title("📽️ Conversational RAG YouTube Chatbot")

    if "last_video_id" not in st.session_state:
        st.session_state.last_video_id = None

    video_url = st.text_input(
        "🎞️ Paste a YouTube Video URL to start a new conversation:"
    )
    question = st.chat_input("💬 Ask a question based on the video transcript:")

    if video_url:
        video_id = video_url.split("v=")[-1].split("&")[0]
        logger.info(f"Fetched video ID from youtube URL: {video_id}")

        if video_id != st.session_state.last_video_id:
            try:
                transcript = fetch_transcript(video_id)
                st.success("Transcript fetched successfully!")
                docs = split_transcript(transcript)
                embeddings = get_embedding_model()
                vector_store = create_vector_store(docs, embeddings)
                logger.debug(f"vector store: {vector_store}")
                retriever = get_retriever(vector_store)
                logger.debug(f"Output from the Retriever: {retriever}")
                st.session_state.chain = build_chain(retriever)
                logger.debug(f"Output of the chain:  {st.session_state.chain}")
                st.session_state.last_video_id = video_id
                clear_chat_history()

            except Exception as e:
                st.error(str(e))
                return

    render_chat()
    logger.debug(f"All the streamlit session state up until NOW: {st.session_state}")
    if question and "chain" in st.session_state:
        try:
            history = load_chat_history()
            logger.info(f"Chat History up until now: {history}")
            response = st.session_state.chain.invoke(question)
            logger.debug(f"The Response from the LLMs: {response}")
            history.append(HumanMessage(content=question))
            history.append(AIMessage(content=response))
            save_chat_history(history)

            with st.chat_message("user"):
                st.markdown(question)
            with st.chat_message("assistant"):
                st.markdown(response)

        except Exception as e:
            st.error(f"Error: {e}")


if __name__ == "__main__":
    main()
