import streamlit as st

def get_llm_model():
    ...

def call_llm_chain(inp):
    ...
def understanding_page():

    # Initialize session state
    if 'code_understanding_generated' not in st.session_state:
        st.session_state['code_understanding_generated'] = []
    if 'code_understanding_past' not in st.session_state:
        st.session_state['code_understanding_past'] = []

    # Create text area to get input from user
    def get_text():
        input_text = st.text_area("You: ", key="input", height=250)
        # Add custom CSS to style it
        st.markdown(f"""
        <style>
        .stTextArea {{
            width: 700px;
            height: 300px;
            font-size: 14px;
            border: 1px solid #ccc;
            padding: 10px;
        }}  
        </style>
        """, unsafe_allow_html=True)    
        return input_text 
    
    user_input = get_text()
    
    if user_input:

        # @TODO: Update with the real llm funciton
        # Run LLM Chain
        output = call_llm_chain(user_input)
        
        # Add generated output to session state history
        st.session_state.code_understanding_past.append(user_input)
        st.session_state.code_understanding_generated.append(output)
        
    # Display History
    if st.session_state['code_understanding_generated']:
                
        for i in range(len(st.session_state['code_understanding_generated'])-1, -1, -1):
            message = st.session_state['code_understanding_generated'][i] 
            st.write("Bot:", message)
            
        for i in range(len(st.session_state['code_understanding_past'])-1, -1, -1):
            message = st.session_state['code_understanding_past'][i]
            st.write("You:", message)