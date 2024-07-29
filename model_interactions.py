# imports
from clients import get_model_client, get_openai_client
from data_mgmt import get_prompt


# Local model
def get_response_from_model(messages=[]):
    if not messages:
        return "Error: No messages provided."
    
    client = get_model_client()
    if client is None:
        return "Error: Model client not found."
    
    # Get the model response
    return client.chat.completions.create(
        model="TheBloke/dolphin-2.5-mixtral-8x7b-GGUF",
        messages=messages,
        temperature=0.7,
        )

# OpenAi API
def get_gpt_response(message, local=False):
    if local:
        client = get_model_client()
    else:
        client = get_openai_client()
    completion = client.chat.completions.create(
        model="gpt-4o", #"gpt-3.5-turbo" or "gpt-4"
        messages=[
            {"role": "system", "content": get_prompt('sys_prompt')},
            {"role": "user", "content": message}
        ]
        )
    return completion.choices[0].message.content