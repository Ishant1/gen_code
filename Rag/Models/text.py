from langchain_google_vertexai import VertexAI
from langchain.embeddings import VertexAIEmbeddings


def get_langchain_llm(model_id: str):
    return VertexAI(model_name=model_id)


def get_langchain_embeddings(model_id: str = "text-bison-32k"):
    return VertexAIEmbeddings(model_id)

model = get_langchain_llm(model_id="text-bison-32k")
print(model.invoke("hi what can you do"))