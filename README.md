# UniGPT 🚀
https://github.com/Hustler-Am-Limit/UniGPT/raw/main/media/readme-demo.mp4

## About
UniGPT 🚀 allows you to ask questions about the University of Vienna and get accurate answers with instant citations.

## Useful links & facts
Source code: this GitHub repo
Data: [Scraped websites of the University of Vienna](https://github.com/Hustler-Am-Limit/UniGPT/blob/main/data/cleaned_english_documents.txt.zip)
Scraping was done on the 27. October 2023 and 24 371 out of ~100 000 English univie.ac.at pages were scraped

## FAQ
### How does UniGPT work?
In a nutshell, UniGPT was fed with scraped websites of the University of Vienna (e.g. univie.ac.at/en, studieren.univie.ac.at/en) and its contents were stored in a vector database that allows for semantic search and retrieval.

When you ask a question, UniGPT will search through the pre-scraped website contents and find the most relevant ones using the vector index. Then, it will use GPT-3.5 to generate a final answer.

### Is my data safe?
No, the data is logged for me to improve the user experience and fix bugs as fast as possible.

### Are the answers 100% accurate?
No.
