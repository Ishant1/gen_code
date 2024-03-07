"""File to implement the langchain pipeline"""
from langchain_google_vertexai import VertexAI

from utils.setup import setup_vertex_ai

setup_vertex_ai(project="qwiklabs-gcp-04-7e74d632994e", location="us", key_json="key.json")


def get_model_response(message: str, model_id: str= "gemini-pro") -> str:
    """get the model response for a text generation model

    :param message: The prompt to the model
    :param model_id: The id/name of the model
    :return: The response from the model
    """
    model = VertexAI(model_name=model_id)
    return model.invoke(message)







