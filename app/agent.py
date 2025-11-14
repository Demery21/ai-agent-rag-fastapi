from langchain.chat_models import ChatOpenAI
from rag import retrieve_context
from config import OPENAI_API_KEY

llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=OPENAI_API_KEY)

def run_agent(query: str):
    context = retrieve_context(query)

    prompt = f"""
    You are an assistant that answers questions based on context.
    Context: {context}
    Question: {query}
    """

    return llm.predict(prompt)
