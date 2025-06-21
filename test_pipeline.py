from src.ingest import load_data
from src.preprocess import clean_text
from src.embed import embed_documents
from src.retriever import setup_retriever
from src.llm_chain import generate_summary
from src.db import save_summary

def run_pipeline():
    data = load_data("data/missions.json")
    clean = clean_text(data)
    embed_documents(clean)
    retriever = setup_retriever()
    summary = generate_summary(retriever, query="What happened in mission 5?")
    save_summary(summary)

if __name__ == "__main__":
    run_pipeline()
