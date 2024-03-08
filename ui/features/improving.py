import streamlit as st

from Rag.Models.prompts import get_prompt_for_testing
from Rag.langchain import get_model_response


def get_model_output():
    return "Hello World"

def improving_page():
    codebase = st.session_state['dataExtractor'].get_all_text()
    input_text = st.text_input("Enter a file name to create unit test: ", key="input file")
    if input_text:
        # @TODO add prompt for 
        unit_test = get_model_response(get_prompt_for_unit_test(codebase, input_text))
        st.write(unit_test)
