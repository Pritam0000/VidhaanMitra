import streamlit as st
from faiss_search import FAISSSearch

st.set_page_config(page_title="VidhaanMitra", page_icon="📜", layout="wide")

# Initialize FAISS search engine
search_engine = FAISSSearch()
search_engine.build_index("data/constitution.txt")  # You can extend with more files

st.title("VidhaanMitra - Chatbot for Indian Constitution & Polity 📖")
st.markdown("Ask me anything about the **Indian Constitution**")

query = st.text_input("Enter your query:")
if query:
    results = search_engine.search(query, top_k=3)
    for result, score in results:
        st.write(f"**Answer:** {result} (Relevance: {score:.4f})")
