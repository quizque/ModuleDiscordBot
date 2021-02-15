from random import randint

# Name of module
NAME = "Rock Paper Scissors Mini-Game"

# Commands that the module provide
COMMANDS = {
    "rps": {
        "description": "Plays rock paper scissors!"
    }
}

# Events to trigger on
EVENTS = ["Initialize", "TextSend"]

# Runs on initialize of module
def Initialize():
    print(f"Loaded {NAME} module!")

async def TextSend(message, client):
    if message.author == client.user:
        return

    rps = ['r', 'p', 's']

    if message.content.startswith('$rps'):
        
        bot_answr = rps[randint(0,2)]

        if message.content.split(" ")[1] == bot_answr:
            await message.channel.send(f'You win! Bot got {bot_answr}')
        else:
            await message.channel.send(f'You lost! Bot got {bot_answr}')