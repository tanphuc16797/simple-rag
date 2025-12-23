from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class RAGMemory:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.memory_store = []
        self.embeddings = []

    def add(self, text):
        emb = self.model.encode([text])
        self.memory_store.append(text)
        self.embeddings.append(emb[0])

    def retrieve(self, query, top_k=1):
        if not self.embeddings:
            return []
        q_emb = self.model.encode([query])[0]
        sims = cosine_similarity([q_emb], self.embeddings)[0]
        idxs = np.argsort(sims)[::-1][:top_k]
        return [self.memory_store[i] for i in idxs]
