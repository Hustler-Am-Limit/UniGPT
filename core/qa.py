from typing import Dict
from langchain.chains import ConversationalRetrievalChain
from core.prompts import PROMPT


def get_qa_with_sources(llm, docsearch, memory) -> ConversationalRetrievalChain:
    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=docsearch.as_retriever(search_kwargs={"k": 3}),
        condense_question_llm=llm,
        return_source_documents=True,
        verbose=True,
        memory=memory,
        combine_docs_chain_kwargs={"prompt": PROMPT},
        # get_chat_history=lambda h : h,
    )
