import streamlit as st

from Rag.Models.prompts import get_prompt_for_learning
from Rag.langchain import get_model_response


def learning_page():
    codebase = st.session_state['dataExtractor'].get_all_text()
    output = get_model_response(get_prompt_for_learning(codebase))
    st.write(output)
