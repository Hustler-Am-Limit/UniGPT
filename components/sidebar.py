import streamlit as st
from components.faq import faq


def sidebar():
    with st.sidebar:
        st.markdown(
            "# How to use\n"
            "1. Enter your secret code below 👇\n"
            "2. Ask a question about the University of Vienna 🏫\n"
            "3. Get your answer 👨‍💻\n"
        )
        unlock_code = st.text_input(
            "Secret code",
            placeholder="Enter your secret code here",
            # value=os.environ.get("OPENAI_API_KEY", None)
            # or st.session_state.get("OPENAI_API_KEY", ""),
        )
        st.session_state["UNLOCK_CODE"] = unlock_code

        st.markdown("---")
        st.markdown("## About")
        st.markdown(
            "UniGPT 🚀 allows you to ask questions about the University of Vienna "
            "and get accurate answers with instant citations. "
        )
        st.markdown("Made by [Ebubekir Şahan](mailto:sahan@ebubekir.at)")
        st.markdown("---")
        st.markdown(
            """
            ## Useful links & facts\n
            Source code: (coming soon)\n
            Data: (coming soon)\n
            Scraping was done on the 27. October 2023 and 24 371 out of ~100 000 English univie.ac.at pages were scraped
            """
        )
        st.markdown("---")

        faq()
