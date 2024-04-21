from openai import OpenAI
from dotenv import load_dotenv
import os

def get_model_client():
    """clients.py method to return the model client object"""
    # Point to the local server
    return OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

def get_openai_client():
    """clients.py method to return the openai client object"""
    # get api key from .env file
    load_dotenv()
    return OpenAI(api_key=os.getenv('openai_key'))