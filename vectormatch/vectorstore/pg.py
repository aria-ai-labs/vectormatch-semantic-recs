import psycopg2
import numpy as np
from sentence_transformers import SentenceTransformer

class PGVectorStore:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.conn = psycopg2.connect(
            dbname="vector_db", user="postgres", password="postgres", host="localhost"
        )

    def similarity_search(self, text: str, k: int = 5):
        vec = self.model.encode(text).tolist()
        with self.conn.cursor() as cur:
            cur.execute(
                "SELECT name, cosine_similarity(embedding, %s) AS sim FROM providers ORDER BY sim DESC LIMIT %s",
                (vec, k)
            )
            return [{"name": row[0], "similarity": row[1]} for row in cur.fetchall()]

def get_pg_vector_store():
    return PGVectorStore()