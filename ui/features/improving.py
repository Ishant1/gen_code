import streamlit as st

from Rag.Models.prompts import get_prompt_for_testing
from Rag.langchain import get_model_response


def get_model_output():
    return "Hello World"

def improving_page():
    codebase = st.session_state['dataExtractor'].get_all_text()
    output = get_model_response(get_prompt_for_testing(codebase))
    st.write(output)