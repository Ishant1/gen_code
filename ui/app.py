import sys

sys.path.append('../gen_code')

from Rag.Dataset.load_dataset import DataExtractor
import streamlit as st
from features.improving import improving_page
from features.learning import learning_page
from features.understanding import understanding_page


if 'status' not in st.session_state.keys():
    st.session_state['status'] = 'ui_started'
if 'github_link' not in st.session_state.keys():
    st.session_state['github_link'] = None
if 'repo_name' not in st.session_state.keys():
    st.session_state['repo_name'] = None
if 'dataExtractor' not in st.session_state.keys():
    st.session_state['dataExtractor'] = None

st.set_page_config(page_title='TBD Coder', page_icon=':smiley:') 

st.sidebar.image('https://images.unsplash.com/photo-1677756119517-756a188d2d94?q=80&w=2950&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', use_column_width=True)
# Get github Link
st.sidebar.header('Enter GitHub Link')
st.session_state['github_link'] = st.sidebar.text_input('GitHub Link')
st.sidebar.header('Enter Repo Name')
st.session_state['repo_name'] = st.sidebar.text_input('Repo Name')

page_navigation = ['Learning', 'Improving', 'Understanding']

def initialize_dataExtractorClass():
    dataExtractor = DataExtractor(st.session_state['github_link'], 'Rag/Dataset/git_repo/{repo_name}'.format(repo_name=st.session_state['repo_name']))
    dataExtractor.get_git_code()
    dataExtractor.load_github_data_from_local()
    st.session_state['status'] = 'repo_cloned'
    return dataExtractor
def reset_session():
    for key in st.session_state.keys():
        del st.session_state[key]
    st.rerun()

if st.session_state['github_link'] and st.session_state['repo_name']:
    if st.session_state['status'] == 'ui_started':
        st.session_state['dataExtractor'] = initialize_dataExtractorClass()
        st.sidebar.success('GitHub Repo Cloned')
else: 
    st.sidebar.error('Please enter GitHub Link and Repo Name')

if st.session_state['status'] == 'repo_cloned':
    st.sidebar.title('Navigation')
    page = st.sidebar.radio('Tasks',  page_navigation)
    if st.sidebar.button("Reset Session"):
        reset_session()
    
    
    if page == page_navigation[0]:
        st.title(page_navigation[0])
        if st.session_state['dataExtractor']:
            learning_page()

    elif page == page_navigation[1]:
        st.title(page_navigation[1])
        improving_page()

    else:
        st.title(page_navigation[2])
        understanding_page()