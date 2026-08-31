from contextlib import asynccontextmanager

from fastapi import FastAPI

from core.preprocessing import ensure_nltk_data


@asynccontextmanager
async def lifespan(app: FastAPI):
    ensure_nltk_data()
    yield


app = FastAPI(
    title="RAG Search Engine API",
    description="Template inicial para a API de busca RAG da aula.",
    version="0.1.0",
    lifespan=lifespan,
)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
