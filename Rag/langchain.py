"""File to implement the langchain pipeline"""
from Rag.Models.VertexAiModels import get_langchain_llm
from utils.setup import setup_vertex_ai
setup_vertex_ai(project="lloyds-genai24lon-2714", location="europe-west2")


def get_model_response(message: str, model_id: str="text-bison-32k") -> str:
    """get the model response for a text generation model

    :param message: The prompt to the model
    :param model_id: The id/name of the model
    :return: The response from the model
    """
    model = get_langchain_llm(model_id=model_id)
    return model.invoke(message)
