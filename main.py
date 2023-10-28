import streamlit as st
from components.sidebar import sidebar
from core.utils import get_llm, get_docsearch, get_conversation_string
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from core.qa import get_qa_with_sources
from langchain.memory import ConversationBufferWindowMemory
from streamlit_chat import message
from langchain.schema import BaseMessage
from streamlit.logger import get_logger
from langchain.docstore.document import Document
from typing import List

logger = get_logger(__name__)


class Results:
    question: str
    chat_history: List[BaseMessage]
    answer: str
    sources: List[Document]

    def __init__(self, question, chat_history, answer, source_documents):
        self.question = question
        self.chat_history = chat_history
        self.answer = answer
        self.source_documents = source_documents


MODEL_LIST = ["debug"]

st.set_page_config(page_title="UniGPT", page_icon="🚀", layout="wide")
st.header("UniGPT 🚀")

with open("style.css") as file:
    st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)

sidebar()
if st.session_state["UNLOCK_CODE"]:
    if st.session_state["UNLOCK_CODE"] == st.secrets["UNLOCK_CODE"]:
        # TODO: add gpt-4
        MODEL_LIST.insert(0, "gpt-3.5-turbo")
        MODEL_LIST.remove("debug")

if "PREV_UNLOCK_CODE" in st.session_state:
    if st.session_state["PREV_UNLOCK_CODE"] != st.session_state["UNLOCK_CODE"]:
        del st.session_state["llm"]
        if "buffer_memory" in st.session_state:
            del st.session_state["buffer_memory"]

st.session_state["PREV_UNLOCK_CODE"] = st.session_state["UNLOCK_CODE"]

model: str = st.selectbox("Model", options=MODEL_LIST)

openai_api_key = st.secrets["OPENAI_API_KEY"]

if not openai_api_key:
    st.warning("OpenAI API Key not found")

if "responses" not in st.session_state:
    st.session_state["responses"] = ["How can I assist you?"]

if "requests" not in st.session_state:
    st.session_state["requests"] = []

response_container = st.container()
question = st.chat_input("Ask a question about the University of Vienna 🫵", key="input")

with response_container:
    if st.session_state["responses"]:
        message(st.session_state["responses"][0], key=str(0))


if "llm" not in st.session_state:
    st.session_state["llm"] = get_llm(
        model=model,
        openai_api_key=openai_api_key,
        temperature=0,
        streaming=True,
        callbacks=[StreamingStdOutCallbackHandler()],
    )

if "docsearch" not in st.session_state:
    st.session_state["docsearch"] = get_docsearch(
        index_name="unigpt-index",
        pinecone_api_key=st.secrets["PINECONE_API_KEY"],
        pinecone_environment=st.secrets["PINECONE_ENVIRONMENT"],
    )

if "buffer_memory" not in st.session_state:
    st.session_state.buffer_memory = ConversationBufferWindowMemory(
        k=3,
        return_messages=True,
        memory_key="chat_history",
        input_key="question",
        output_key="answer",
    )

result = get_qa_with_sources(
    llm=st.session_state["llm"],
    docsearch=st.session_state["docsearch"],
    memory=st.session_state["buffer_memory"],
)

# with textcontainer:
if question:
    # question = st.text_input("Question: ", key="input")
    # if question:
    with st.spinner("thinking..."):
        conversation_string = get_conversation_string()
        # st.code(conversation_string)
        # refined_query = query_refiner(conversation_string, query)
        # st.subheader("Question:")
        # st.write(question)
        # context = find_match(refined_query)
        # print(context)
        response = Results(
            **result({"question": question, "chat_history": conversation_string})
        )
    st.session_state.requests.append(question)
    st.session_state.responses.append(response)
with response_container:
    # skip first generic response by AI
    for i in range(len(st.session_state["responses"])):
        if st.session_state["responses"]:
            if hasattr(st.session_state["responses"][i], "answer"):
                sources: str = "\nSources:\n"
                for j, source_doc in enumerate(
                    st.session_state["responses"][i].source_documents
                ):
                    # if title should be missing, replace the text of the hyperlink with a number
                    sources += f'{j+1}: [{source_doc.metadata["title"] if source_doc.metadata["title"] != None and len(str.strip(source_doc.metadata["title"])) else j+1}]({source_doc.metadata["source"]}) '
                message(
                    f'{st.session_state["responses"][i].answer}\n{sources}', key=str(i)
                )
            else:
                if i:
                    message(st.session_state["responses"][i], key=str(i))

            if i < len(st.session_state["requests"]):
                message(
                    st.session_state["requests"][i], is_user=True, key=str(i) + "_user"
                )
