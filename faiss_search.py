from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class FAISSSearch:
    def __init__(self):
        self.model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
        self.index = faiss.IndexFlatL2(384)  # Vector size for MiniLM embeddings

    def build_index(self, data_path):
        """Load data, encode it, and build FAISS index."""
        with open(data_path, "r", encoding="utf-8") as f:
            self.sentences = [line.strip() for line in f if line.strip()]
        
        embeddings = self.model.encode(self.sentences)
        self.index.add(np.array(embeddings))

    def search(self, query, top_k=1):
        """Search the FAISS index for a given query."""
        query_vector = self.model.encode([query])
        distances, indices = self.index.search(np.array(query_vector), top_k)
        return [(self.sentences[i], distances[0][idx]) for idx, i in enumerate(indices[0])]

if __name__ == "__main__":
    search_engine = FAISSSearch()
    search_engine.build_index("data/constitution.txt")
    result = search_engine.search("What is Article 14?")
    print(result)
