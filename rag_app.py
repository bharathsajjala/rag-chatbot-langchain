import os
import gradio as gr
from langchain_community.vectorstores import Chroma
from langchain_community.chat_models import ChatOpenAI   # or `from langchain_openai import ChatOpenAI`
from langchain_community.embeddings import OpenAIEmbeddings 
from langchain.agents.middleware import dynamic_prompt, ModelRequest
from langchain.agents import create_agent
from dotenv import load_dotenv
load_dotenv()

# Load 
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
db = Chroma(
    persist_directory="vectorstore",
    embedding_function=embeddings
)


@dynamic_prompt
def prompt_with_context(request: ModelRequest) -> str:
    """Inject context into state messages."""

    print("Number of messages in the request:", len(request.messages))

    print(len(request.messages))
    last_query = request.state["messages"][-1].text
    retrieved_docs = db.similarity_search(last_query)

    docs_content = "\n\n".join(doc.page_content for doc in retrieved_docs)

    system_message = (
        "You are a helpful assistant. Use the following context in your response:"
        f"\n\n{docs_content}"
    )

    return system_message

# LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0,streaming=True)

agent = create_agent(llm, tools=[], middleware=[prompt_with_context])

def answer_question(query):
   
    ai_response = agent.invoke({"messages": query}) 
    print(ai_response["messages"][-1].text)
    return ai_response["messages"][-1].text

# Gradio UI
ui = gr.Interface(
    fn=answer_question,
    inputs="text",
    outputs="text",
    title="RAG Chatbot using LangChain + ChromaDB"
)

if __name__ == "__main__":
    ui.launch()
