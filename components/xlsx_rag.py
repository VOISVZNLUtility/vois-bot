import pandas as pd
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain.chains import RetrievalQA

def load_xlsx_as_docs(file_path):
    df = pd.read_excel(file_path)
    docs = [Document(page_content=row.to_json()) for _, row in df.iterrows()]
    return docs

def build_rag_chain(file_path, model="llama3"):
    docs = load_xlsx_as_docs(file_path)
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = splitter.split_documents(docs)
    embedder = OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = FAISS.from_documents(split_docs, embedder)
    retriever = vectorstore.as_retriever()
    llm = Ollama(model=model)
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)