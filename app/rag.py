import faiss
from sentence_transformers import SentenceTransformer
import os

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load documents
docs_folder = "../data/docs"
documents = []

for file in os.listdir(docs_folder):
    with open(os.path.join(docs_folder, file), "r", encoding="utf-8") as f:
        documents.append(f.read())

# Create embeddings
vectors = model.encode(documents)
index = faiss.IndexFlatL2(vectors.shape[1])
index.add(vectors)

def retrieve_context(query: str) -> str:
    q_vec = model.encode([query])
    _, idx = index.search(q_vec, 1)
    return documents[idx[0][0]]
