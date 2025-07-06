from fastapi import FastAPI
from vectormatch.api.v1 import router

app = FastAPI(title="VectorMatch")
app.include_router(router, prefix="/v1")