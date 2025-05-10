from langchain_core.prompts import PromptTemplate


def get_prompt_template():
    return PromptTemplate(
        template="""
          You are a helpful assistant.
          Answer ONLY from the provided transcript context.
          If the context is insufficient, just say you don't know.

          {context}
          Question: {question}
        """,
        input_variables=["context", "question"]
    )


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)