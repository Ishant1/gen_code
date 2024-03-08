import streamlit as st

def get_model_output():
    return "Hello World"

def learning_page():
    data = get_model_output()
    st.write(data)