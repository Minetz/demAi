import streamlit as st
from data_mgmt import get_pickled_data

def welcome_page():
    """Welcome page for the app"""
    st.title("<App Title>")
    st.markdown("<Some markdown>")

    # Loading
    with st.spinner('Wait for it...'):
        # Load required data
        if st.session_state['<data state>'] == []:
            st.session_state['<data state>'] = get_pickled_data()    
    
    st.success('<Success>')


    start_button = st.button("Start")

    if start_button:
        st.session_state['current_page'] = "<first_page_name>"
        st.rerun()
