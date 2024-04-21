import streamlit as st
from clients import get_model_client
from data_mgmt import response_to_json
from model_interactions import get_response_from_model


def generate_questions():
    """Generate questions for the user"""

    model = get_model_client()
    if model is None:
        return "Error: Model client not found."
    
    questions_from_model = get_response_from_model(st.session_state['messages'])
    parsed_questions = response_to_json(questions_from_model.choices[0].message.content)
    return parsed_questions
