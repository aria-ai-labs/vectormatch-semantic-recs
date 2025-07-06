from fastapi import APIRouter
from vectormatch.pipeline.query import search_similar
from pydantic import BaseModel

router = APIRouter()

class Query(BaseModel):
    text: str

@router.post("/search")
def search(q: Query):
    results = search_similar(q.text)
    return {"results": results}