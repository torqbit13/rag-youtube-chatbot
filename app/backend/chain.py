from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough,
)
from langchain_google_genai import ChatGoogleGenerativeAI
from utils.helpers import format_docs, get_prompt_template

from backend.config import GOOGLE_API_KEY
from backend.history import load_chat_history


def build_chain(retriever):
    prompt = get_prompt_template()
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-8b", google_api_key=GOOGLE_API_KEY)

    return (
        RunnableParallel(
            {
                "context": retriever | RunnableLambda(format_docs),
                "question": RunnablePassthrough(),
                "chat_history": RunnableLambda(lambda _: load_chat_history()),
            }
        )
        | prompt
        | llm
        | StrOutputParser()
    )
