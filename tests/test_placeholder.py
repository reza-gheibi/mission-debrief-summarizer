from src.ingest import load_data
from src.preprocess import clean_text
from src.embed import embed_documents
from src.retriever import setup_retriever
from src.llm_chain import generate_summary
from src.db import save_summary

def test_placeholder():
    data = [{"log": "This is a test mission."}]
    cleaned = clean_text(data)
    embed_documents(cleaned)
    retriever = setup_retriever()
    summary = generate_summary(retriever, query="Test query?")
    save_summary(summary)
    assert isinstance(summary, str)

if __name__ == "__main__":
    run_pipeline()
