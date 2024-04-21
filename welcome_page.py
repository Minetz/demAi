import streamlit as st
from data_mgmt import get_session_questions

def welcome_page():
    """Welcome page for the app"""
    st.title("demAi")
    st.markdown(st.session_state['welcome_message'])
    
    with st.spinner('Wait for it...'):
        if st.session_state['generated_questions'] == []:
            st.session_state['generated_questions'] = get_session_questions()    
    
    st.success('Questions generated!')


    start_button = st.button("Start")

    if start_button:
        st.session_state['current_page'] = "question_page"
        st.rerun()
