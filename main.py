from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.environ["PASCAL_KEY"])

assistant = client.beta.assistants.retrieve(assistant_id="asst_pjOwrgeGnK2EkakZ1Tx3GULc")


if __name__ == "__main__":
    pass    
