from dotenv import load_dotenv
from typing import List, Dict, Final
import os
from discord import Intents, Client, Message
from responses import get_response

#Load env variables
load_dotenv()
DISCORD_TOKEN :Final[str] = os.environ["DISCORD_TOKEN"]

#BOT SETUP

intents: Intents = Intents.default()
intents.message_content = True
discord_client: Client = Client(intents=intents)

#MESSAGE FUNCTIONALITY

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("Message was empty-> intents not set properly")
        return
    
    if is_private := user_message[0]=="?":
        user_message = user_message[1:]

    try:
        response: str = get_response(user_input=user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print("".format(e))


# BOT STARTUP

@discord_client.event

async def on_ready()-> None:
    print(f"{discord_client.user} is running")

@discord_client.event

async def on_message(message: Message)-> None:
    if message.author == discord_client.user:
        return
    username: str = str(message.author)
    user_message: str = message.content
    channel:str = str(message.channel)
    
    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)
    
    
# MAIN ENTRY POINT

def main()-> None:
    discord_client.run(DISCORD_TOKEN)
    
if __name__ == "__main__":
    main()


