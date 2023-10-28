from langchain.chat_models import ChatOpenAI
from core.debug import FakeChatModel
from langchain.chat_models.base import BaseChatModel
from langchain.vectorstores import Pinecone
from langchain.embeddings import HuggingFaceEmbeddings
import pinecone
import streamlit as st

def get_llm(model: str, **kwargs) -> BaseChatModel:
    if model == "debug":
        return FakeChatModel()
    else:
        return ChatOpenAI(model=model, **kwargs)


def get_docsearch(index_name: str, pinecone_api_key: str, pinecone_environment: str):
    # initialize pinecone
    pinecone.init(api_key=pinecone_api_key, environment=pinecone_environment)
    # use bge-small instead of bge-large
    #hf_embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-large-en-v1.5")
    hf_embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")

    return Pinecone.from_existing_index(index_name, hf_embeddings)

def get_conversation_string():
    conversation_string = ""
    for i in range(len(st.session_state['responses'])-1):
        
        conversation_string += "Human: "+st.session_state['requests'][i] + "\n"
        conversation_string += "AI: "+ st.session_state['responses'][i+1].answer + "\n"
    return conversation_string

# @st.cache_resource
# def init_memory() -> ConversationBufferWindowMemory:
#     return ConversationBufferWindowMemory(
#         k=3,
#         return_messages=True,
#         memory_key="chat_history",
#         input_key="question",
#         output_key="answer",
#     )
