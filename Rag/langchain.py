"""File to implement the langchain pipeline"""
from langchain_google_vertexai import VertexAI
from langchain.embeddings import VertexAIEmbeddings

from utils.setup import setup_vertex_ai

setup_vertex_ai(project="lloyds-genai24lon-2714", location="europe-west2")


from Rag.Models.VertexAiModels import get_langchain_llm, get_langchain_embeddings



def get_model_response(message: str, model_id: str="gemini-pro") -> str:
    """get the model response for a text generation model

    :param message: The prompt to the model
    :param model_id: The id/name of the model
    :return: The response from the model
    """
    model = VertexAI()
    return model.invoke(message)











