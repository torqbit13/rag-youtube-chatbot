from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough,
)
from langchain_google_genai import ChatGoogleGenerativeAI

from backend.config import GOOGLE_API_KEY
from utils.helpers import format_docs, get_prompt_template


def build_chain(retriever):
    prompt = get_prompt_template()
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-8b", google_api_key=GOOGLE_API_KEY)

    parallel_chain = RunnableParallel({
        "context": retriever | RunnableLambda(format_docs),
        "question": RunnablePassthrough()
    })

    return parallel_chain | prompt | llm | StrOutputParser()