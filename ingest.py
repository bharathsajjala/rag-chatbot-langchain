import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import getpass
import os
from dotenv import load_dotenv

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")

def ingest():
    # Load PDF
    loader = PyPDFLoader("data/Solar-System-GK-Notes-in-PDF.pdf")
    docs = loader.load()

    # Chunk text
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=150
    )
    chunks = splitter.split_documents(docs)

    # Embed + store in Chroma
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="vectorstore"
    )

    print("✅ Ingestion completed! Vector DB created at /vectorstore")

if __name__ == "__main__":
    ingest()
