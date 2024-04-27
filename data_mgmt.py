import os
import pickle
from dotenv import load_dotenv


def get_env_var(name=""):
    """clients.py method to return a variable in the .env file of the project"""
    load_dotenv()
    if name:
        return os.getenv(name)
    else:
        return None
    
def get_sys_prompt():
    """clients.py method to return a prompt for the model to generate a response to."""
    return """You are a kind assistant which keep people company."""

def get_welcome_message():
    """clients.py method to return a Welcome message for the home screen."""
    return """<Your welcom message for the home screen>"""

def get_prompt(text):
    """A functions which takes input to build a prompt to send to the model."""
    
    return f"""Our user says: {text}"""

def get_pickled_data():
    """This functions reads the pickle file in app/data/pickled_data.pkl
    and returns a random element from that list."""
    with open("data/pickled_data.pkl", "rb") as f:
        questions = pickle.load(f)
    return questions
