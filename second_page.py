import streamlit as st
from data_mgmt import get_prompt
from model_interactions import get_gpt_response


def second_page():
    """Second page for the app"""
    st.title("<Send user input to model>")
    # Build a prompt
    prompt = get_prompt(st.session_state['user_input'])
    st.write(f"Prompt: \n{prompt}")
    # Send the prompt to the model
    with st.spinner('Please wait... Model is generating a response.'):
        if st.session_state['response'] == "":
            st.session_state['response'] = get_gpt_response(prompt)
    
    st.write(f"Response: \n{st.session_state['response']}")

    # Add a button to generate the report
    last_page_button = st.button("<Last page>")
    if last_page_button:
        st.session_state["current_page"] = "welcome_page"
        st.rerun()

