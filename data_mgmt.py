import os
import random
import pickle
from dotenv import load_dotenv


def get_env_var(name=""):
    """clients.py method to return a variable in the .env file of the project"""
    load_dotenv()
    if name:
        return os.getenv(name)
    else:
        return None
    
def get_prompt(name=""):
    """clients.py method to return a prompt for the model to generate a response to.
Options are:
    - sys_prompt
    - start_user_prompt
    - welcome_message"""

    if name == "":
        return None

    if name == "sys_prompt":
        return """You are an expert psychologist in understanding personality traits. The goal of this app is to help users understand their political views by analysing their personality traits and political views based on the answers to the questions they provide."""

    elif name == "welcome_message":
        return """Welcome to demAi! This app helps you explore your political views by asking you a series of questions.
Each question is designed to help highlight traits of your personality (using the OCEAN or Big Five personality model).
At each step, we'll tell you how your answer is related to your personality traits and which personality traits would have answered differently.

We **DO NOT** store any of your responses. Your privacy is important to us. Let's get started!"""

    return None

def get_analysis_prompt(question, answer):
    """clients.py method to return a prompt for the model to generate a response to.
    This prompt is used in the analysis_page.py file."""
    
    return f"""You are an expert psychologist in understanding personality traits. 
You have been asked to analyze the following questions and answers to determine the personality traits of the respondent.
With the given question, trait and answer give a score from 1 to 5 on how much the answer reflects the trait.
Return your answer in the following format:
Score: < int from 1 to 5 extremes included >
Trait: < the trait you with to assess >
Explaination: < explaination of the score >

Question:{question['Question']}

Answer: {answer}

Do not generate any other question. Analyse only the question and answer given.
"""

def get_report_prompt(questions, answers, analysis)->str:
    """clients.py method to return a prompt for the model to generate a response to.
    This prompt is used in the analysis_page.py file."""
    
    return f"""You are an expert psychologist in understanding personality traits.
Your goal is to provide a short but insightful report assessing the political leaning of the respondent.
The information you have available is the questions asked, the answers given and the analysis of the answers (analysis you provided).
Question 1: {questions[0]['Question']}
Answer given by user: {answers[0]}
Analysis of response: {analysis[0]}

Question 2: {questions[1]['Question']}
Answer given by user: {answers[1]}
Analysis of response: {analysis[1]}

Question 3: {questions[2]['Question']}
Answer given by user: {answers[2]}
Analysis of response: {analysis[2]}

Based on the information provided, write a short report on the political leaning of the respondent, no longer than a paragraph.
The questions where designed by you, so if the answers are not clear or do not have enough detail, please make an assumption based on the information provided.
At the end add a best guess of the political leaning with the format "Best guess: <political leaning>"
"""



def response_to_json(remaining_response="", debug=False)->list:
    if remaining_response is None:
        return []
        
    jsons = []
    for i in range(2,5):
        if debug: print(i-1)
        # get question
        if i == 4:
            if debug: print(remaining_response)
            question = remaining_response
        elif i == 2:
            question, remaining_response = remaining_response.split(f"{i}. ")
            question = question.split("1. ")[1]    
        else:
            question, remaining_response = remaining_response.split(f"{i}. ")
        

        # get examples
        question, remaining = question.split("a. ")
        example_a, example_b = remaining.split("b. ")
        # get personality trait
        example_a,part = example_a.split("(")
        trait_a = part.split(")")[0]
        example_b,part = example_b.split("(")
        trait_b = part.split(")")[0]

        json_i = {
            "Question"     : question,
            "example_a"    : {"text" : example_a, "trait":trait_a},
            "example_b"    : {"text" : example_b, "trait":trait_b}
            
        }
        jsons.append(json_i)
        if debug: print(json_i)       
        if debug: print("---")
    return jsons



def get_session_questions():
    """This functions reads the pickle file in app/data/generated_questions.pkl
    and returns a random element from that list."""
    with open("data/generated_questions.pkl", "rb") as f:
        questions = pickle.load(f)
    return random.choice(questions)
