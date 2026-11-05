# Multi-Agent Research Assistant

A small, transparent research workflow that creates a cited Markdown brief from local source cards. It is deliberately dependency-free and works offline.

## Agents

1. Research Agent retrieves relevant source cards.
2. Analyst Agent extracts key findings.
3. Critic Agent removes findings without source traceability.
4. Writer Agent creates a cited Markdown report.

## Run

```bash
python app.py "How can AI improve 5G network optimisation?"
```

## Next improvements

- Use a web-search API and store sources in ChromaDB/FAISS.
- Add PDF ingestion and RAG citations with page numbers.
- Add an LLM as the Analyst/Writer Agent.
- Evaluate citation precision and answer quality on test questions.
