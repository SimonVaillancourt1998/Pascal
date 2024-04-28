from openai import OpenAI
import time
import os
import logging
from typing import Final

# Configure logging
logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s')

# Openai key
OPENAI_KEY: Final[str] = os.environ["PASCAL_OPENAI_TOKEN"]
PASCAL_ID: Final[str] = "asst_pjOwrgeGnK2EkakZ1Tx3GULc"

openai_client = OpenAI(api_key=OPENAI_KEY)

assistant = openai_client.beta.assistants.retrieve(assistant_id=PASCAL_ID)

def create_thread():
    thread = openai_client.beta.threads.create()
    return thread.id

def insert_input(thread_id,message_body) -> str:
    try:
        message = openai_client.beta.threads.messages.create(
            thread_id= thread_id,
            role="user",
            content=message_body
        )
        return message.id
    except Exception as e:
        logging.error(f"Error occurred while inserting input: {e}")

def run_assistant(thread_id) -> str:
    try:
        # Run the assistant
        run = openai_client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant.id,
            instructions="Response must be 1000 or fewer characters in length"
        )

        # Wait for completion
        while run.status != "completed":
            # Be nice to the API
            time.sleep(0.5)
            run = openai_client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)

        # Retrieve the Messages
        messages = openai_client.beta.threads.messages.list(thread_id=thread_id)
        new_message = messages.data[0].content[0].text.value # type: ignore
        logging.info(f"[Pascal]: {new_message}")
        return new_message
    except Exception as e:
        logging.error(f"Error occurred while running assistant: {e}")

def get_response(thread_id, user_input: str) -> str:
    insert_input(thread_id, user_input)
    try:
        message = run_assistant(thread_id)
        return message
    except Exception as e:
        logging.error(f"Error occurred while getting response: {e}")
        return f"I'm sorry, the following issue occurred: {e}"
