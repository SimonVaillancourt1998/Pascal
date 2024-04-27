from openai import OpenAI
from dotenv import dotenv

env = dotenv()

client = OpenAI(api_key=env.PASCAL_KEY)

assistant = client.beta.assistants.retrieve(assistant_id="asst_pjOwrgeGnK2EkakZ1Tx3GULc")


if __name__ == "__main__":
    pass    
