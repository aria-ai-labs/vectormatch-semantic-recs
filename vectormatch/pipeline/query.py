from vectormatch.vectorstore.pg import get_pg_vector_store

def search_similar(query: str, top_k: int = 5):
    store = get_pg_vector_store()
    return store.similarity_search(query, k=top_k)