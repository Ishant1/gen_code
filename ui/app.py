import streamlit as st
from features.improving import improving_page
from features.learning import learning_page
from features.understanding import understanding_page

st.set_page_config(page_title='TBD Coder', page_icon=':smiley:') 

st.sidebar.image('https://images.unsplash.com/photo-1677756119517-756a188d2d94?q=80&w=2950&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', use_column_width=True)
# Get github Link
st.sidebar.header('Enter GitHub Link')
github_link = st.sidebar.text_input('GitHub Link')

page_navigation = ['Learning', 'Improving', 'Understanding']

def reset_session():
    for key in st.session_state.keys():
        del st.session_state[key]
    st.rerun()
if github_link:
    st.sidebar.success('GitHub Link Saved')
    st.sidebar.title('Navigation')
    page = st.sidebar.radio('Tasks',  page_navigation)
    if st.sidebar.button("Reset Session"):
        reset_session()
    if page == page_navigation[0]:
        st.title(page_navigation[0])
        learning_page()

    elif page == page_navigation[1]:
        st.title(page_navigation[1])
        improving_page()

    else:
        st.title(page_navigation[2])
        understanding_page()
    
else: 
    st.sidebar.error('Please enter GitHub Link')

