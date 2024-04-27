import streamlit as st
from data_mgmt import get_prompt
from welcome_page import welcome_page
from question_page import question_page
from analysis_page import analysis_page

def init_session_state():
    if 'analysis' not in st.session_state:
        st.session_state['analysis'] = []
    if 'report' not in st.session_state:
        st.session_state['report'] = False
    if 'question_number' not in st.session_state:
        st.session_state['question_number'] = 0
    if 'responses' not in st.session_state:
        st.session_state['responses'] = []
    if 'messages' not in st.session_state:
        st.session_state['messages'] = [
            {"role": "system", "content": get_prompt('sys_prompt')},
            {"role": "user", "content": get_prompt('start_user_prompt')}
            ]
    if 'generated_questions' not in st.session_state:
        st.session_state['generated_questions'] = []
    if 'welcome_message' not in st.session_state:
        st.session_state['welcome_message'] = get_prompt('welcome_message')
    if 'current_page' not in st.session_state:
        st.session_state['current_page'] = "welcome_page"


def main():
    init_session_state()
    if st.session_state['current_page'] == "welcome_page":
        welcome_page()
    elif st.session_state['current_page'] == "question_page":
        question_page()
    elif st.session_state['current_page'] == "analysis_page":
        analysis_page()



if __name__ == "__main__":
    main()