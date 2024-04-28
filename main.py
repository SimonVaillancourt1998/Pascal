from dotenv import load_dotenv
from typing import Final
import os
from discord import Intents, Client, Message
from responses import get_response, create_thread
import asyncio  # Import asyncio for handling asynchronous tasks

# Load env variables
load_dotenv()
DISCORD_TOKEN: Final[str] = os.environ["DISCORD_TOKEN"]

# BOT SETUP

intents: Intents = Intents.default()
intents.message_content = True
discord_client: Client = Client(intents=intents)
thread_id = create_thread()


# MESSAGE FUNCTIONALITY

async def send_message(message: Message, user_message: str) -> None:
    
    if not user_message:
        print("Message was empty-> intents not set properly")
        return
    
    if user_message[0] != "!":
        print("Pascal was not called")
        return
    
    if is_private := user_message[1] == "?":
        user_message = user_message[2:]
    
    # Trigger typing status
    async with message.channel.typing():
        # await asyncio.sleep(2)  # Simulate some processing time
        
        try:
            response: str = get_response(thread_id, user_input=user_message)
            await message.author.send(response) if is_private else await message.channel.send(response)
        except Exception as e:
            print("Error occurred: {}".format(e))
        


# BOT STARTUP

@discord_client.event
async def on_ready() -> None:
    print(f"{discord_client.user} is running")

@discord_client.event
async def on_message(message: Message) -> None:
    if message.author == discord_client.user:
        return
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    
    print(f'[{channel}] {username}: "{user_message}"')
    
    await send_message(message, user_message)

# MAIN ENTRY POINT

def main() -> None:
    discord_client.run(DISCORD_TOKEN)

if __name__ == "__main__":
    main()
