from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


def get_prompt_template():
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful assistant. Answer ONLY from the provided transcript context.\n\n{context}\n\n" "If the context is insufficient, say you don't know.",
            ),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{question}"),
        ]
    )


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)
