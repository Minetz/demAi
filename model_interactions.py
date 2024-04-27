# imports
import streamlit as st
from clients import get_lm_studio_client, get_openai_client

# OpenAi API
def get_gpt_response(message, local=True):
    if local:
        client = get_lm_studio_client()
    else:
        client = get_openai_client()

    # Add the message to the session state
    st.session_state['gpt_messages'].append({"role": "user", "content": message})
    # Request a response from the model    
    completion = client.chat.completions.create(
        model="TheBloke/dolphin-2.5-mixtral-8x7b-GGUF", #"gpt-3.5-turbo" or "gpt-4" or "TheBloke/dolphin-2.5-mixtral-8x7b-GGUF"
        messages=st.session_state['gpt_messages']
        )
    return completion.choices[0].message.content


