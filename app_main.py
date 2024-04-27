import streamlit as st
from data_mgmt import get_sys_prompt, get_welcome_message
from welcome_page import welcome_page
from first_page import first_page
from second_page import second_page

def init_session_state():
    if 'user_input' not in st.session_state:
        st.session_state['user_input'] = []
    if 'response' not in st.session_state:
        st.session_state['response'] = ""
    if 'gpt_messages' not in st.session_state:
        st.session_state['gpt_messages'] = [
            {"role": "system", "content": get_sys_prompt()}
            ]
    if '<data state>' not in st.session_state:
        st.session_state['<data state>'] = []
    if 'welcome_message' not in st.session_state:
        st.session_state['welcome_message'] = get_welcome_message()
    if 'current_page' not in st.session_state:
        st.session_state['current_page'] = "welcome_page"


def main():
    init_session_state()
    if st.session_state['current_page'] == "welcome_page":
        welcome_page()
    elif st.session_state['current_page'] == "<first_page_name>":
        first_page()
    elif st.session_state['current_page'] == "<second_page_name>":
        second_page()



if __name__ == "__main__":
    main()