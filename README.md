# rag-chatbot-langchain
rag-chatbot-langchain
RAG Chatbot using LangChain, Gradio & Local VectorStore

A fully local Retrieval-Augmented Generation (RAG) chatbot built using LangChain, Gradio, and a persistent Chroma vectorstore.
This project allows you to ingest documents, generate embeddings, index them into a vector database, and chat with your private data securely.

🚀 Features

🔍 Document Ingestion Pipeline (ingest.py)

🧠 Embeddings + Vectorstore (Chroma)

🤖 LangChain RetrievalQA / RAG pipeline

💬 Interactive Gradio Chat UI

📁 Local persistent vector store (no cloud dependency)

⚡ Fast query response using semantic search

🔐 Supports private document Q&A securely

📂 Project Structure
rag-chatbot-langchain/
│── data/               # Your PDFs / text files go here
│── vectorstore/        # Persistent Chroma DB
│── ingest.py           # Script to ingest data
│── rag_app.py          # Gradio RAG chatbot
│── requirements.txt
│── .env
│── README.md

🧩 Architecture
End-to-End Flow

Document Ingestion

Loads PDFs/text files from /data

Splits text into chunks

Creates embeddings (OpenAI / OCI / HuggingFace)

Stores vectors in ChromaDB

Chat Query

User sends question via Gradio

Query gets embedded

Vectorstore retrieves relevant chunks

RAG Answer

Retrieved context + question → LLM

LLM produces grounded, accurate response

Response streamed back to Gradio
