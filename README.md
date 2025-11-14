# AI Agent with RAG + FastAPI

This project is a simple, production-ready template for building an **AI Agent** using:

- **FastAPI** for backend API
- **LangChain** for LLM orchestration
- **FAISS** for vector search
- **SentenceTransformers** for embeddings
- **OpenAI API** for language generation

It demonstrates how to build an end-to-end agent pipeline:

1. Load documents  
2. Generate embeddings  
3. Perform vector search (RAG)  
4. Pass retrieved context to an LLM  
5. Serve responses via a FastAPI endpoint  

---

##Running the API

### 1. Install requirements


### 2. Set your OpenAI API key
Create a `.env` file:

### 3. Start FastAPI

### 4. Test the Agent
Send a POST request:


---

## 🧠 How It Works

### RAG Pipeline
- Documents are embedded with `sentence-transformers`
- FAISS performs similarity search
- The most relevant context is passed to the LLM
- Agent generates a final answer

### Tech Used

- Python
- FastAPI
- LangChain
- FAISS
- Sentence Transformers
- OpenAI API

---

## 📌 Notes
This repo is designed to be **simple, readable, and interview-friendly**.
You can extend it by:
- Adding more documents
- Integrating tools
- Adding memory
- Deploying on cloud providers

---

## 📄 License
MIT License

