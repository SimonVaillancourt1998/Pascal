from random import choice, randint


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    
    
    #TODO: implement chatgpt logic
    
    if lowered == "":
        return "I didn't hear that"
    elif lowered == "hello":
        return "Hello there"
    else:
        return "Fuck bitches, get money"