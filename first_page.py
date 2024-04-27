import streamlit as st

def first_page():
    """First page for the app"""
    st.title("<Collect input from user page>")

    # Add a text input or things to do in this page
    with st.form("<Form module>"):
       # How to collect imput from the user 
        answer = st.text_area("<Question>", "Hello there!")
        submitted = st.form_submit_button("Submit answer")
        # If the submit button is clicked
        if submitted:
            # Add the user input to the session state
            st.session_state["user_input"].append(answer)
            # Change the current page to the next page
            st.session_state["current_page"] = "<second_page_name>"
            st.rerun()