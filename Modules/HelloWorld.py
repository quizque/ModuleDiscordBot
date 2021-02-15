
# Name of module
NAME = "Example Module"

# Commands that the module provide
COMMANDS = {
    "hello": {
        "description": "Prints 'Hello World!'"
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

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')