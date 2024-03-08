"""File to help setup GCP connection and apis"""
import os
import vertexai


def setup_vertex_ai(
    project: str=None,
    location: str=None,
    # key_json: str = "key.json"
)-> None:
    """Setup vertex-ai and gcp connection

    This method uses the credential json file to build gcp connection
    and then sets up vertex ai with given project and location.

    Remember to enable vertex-ai and AI prediction api

    :param project: ID of the associated project
    :param location: location of vertex ai, as us or uk
    :param key_json: Address of the json file
    :return: None
    """
    # if not os.path.exists(key_json):
    #     ValueError("Please add authentication credentials json to root folder")

    if not project:
        project = os.getenv("PROJECT_ID")
    if not location:
        location = os.getenv("LOCATION")

    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_json
    vertexai.init(project=project, location=location)


    