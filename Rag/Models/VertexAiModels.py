from langchain_google_vertexai import VertexAI
from langchain.embeddings import VertexAIEmbeddings


def get_langchain_llm(model_id: str):
    return VertexAI(model_name=model_id)


def get_langchain_embeddings(model_id: str = None):
    return VertexAIEmbeddings(model_id)

