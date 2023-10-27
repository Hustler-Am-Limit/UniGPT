import streamlit as st


def faq():
    st.markdown(
        """
## FAQ
### How does UniGPT work?
In a nutshell, UniGPT was fed with scraped websites of the University of Vienna (e.g. univie.ac.at/en or studieren.univie.ac.at/en) 
and its contents were stored in a vector database that allows for semantic search and retrieval.

When you ask a question, UniGPT will search through the
pre-scraped website content chunks and find the most relevant ones using the vector index.
Then, it will use GPT-3.5 to generate a final answer.

### Is my data safe?
No, the data is logged for me to improve the user experience and fix bugs as fast as possible.

### Are the answers 100% accurate?
No.

""")

    expander = st.expander("## Disclaimer")
    expander.write("""
1. **No Liability:** The creator of this chatbot is not liable for any damages, direct or indirect, resulting from the use of this chatbot, including but not limited to any inaccuracies, errors, or omissions in the information provided.
2. **No Warranty or Guarantee:** The information provided by the chatbot is based on scraped content from the University of Vienna's website and is provided "as is" without any warranties, express or implied, including the implied warranties of merchantability, fitness for a particular purpose, or non-infringement. The creator does not warrant that the chatbot will operate error-free or that the information provided will be accurate, complete, or timely.
3. **No Official Affiliation:** This chatbot is not officially affiliated with, endorsed by, or in any way officially connected with the University of Vienna. Any references to the University of Vienna are solely for informational purposes and do not imply any official status or recognition.
4. **Not a Substitute for Official Information:** The chatbot is intended for informational purposes only and should not be relied upon as an official source of information from the University of Vienna. Users are strongly encouraged to consult the official University of Vienna website or contact the relevant department directly for authoritative information.
5. **Updates and Changes:** The content sourced from the University of Vienna's website is subject to change without notice. The chatbot may not reflect the most current information available from the University. The creator is under no obligation to update or maintain the chatbot in light of such changes.
6. **Indemnification:** By using this chatbot, you agree to indemnify and hold harmless the creator from any claims, damages, liabilities, or expenses arising out of your use or reliance on the information provided by the chatbot.
7. **Governing Law:** This disclaimer is governed by the laws of Austria, and any disputes arising out of or in connection with this disclaimer shall be subject to the exclusive jurisdiction of the courts of Austria.

By using UniGPT, you acknowledge that you have read, understood, and agree to be bound by the terms of this disclaimer. If you do not agree with these terms, please refrain from using the chatbot.
""")