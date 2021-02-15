import discord
import Config
import ModuleLoader
import Logging as log

active_modules = {}

def Initilize(client):

    log.setVerbose(log.VERBOSE_HIGH)

    log.printV("Loading module discord bot.")


    log.printV("Checking config file...")
    cfg = Config.load("default.cfg")

    if cfg == None:
        log.printV("No config was found or there was an error!", log.VERBOSE_HIGH)

        if input("> Would you like to make a default.cfg? (y/n) ").lower().strip() == 'y':
            Config.writeExample("default.cfg")
            log.printV("Example config has been writen, fill it out and relaunch the bot!")
            exit()
        
    if not Config.check(cfg):
        log.printV("The config was invalid!", log.VERBOSE_HIGH)

        if input("> Would you like to remake the default.cfg? (y/n) ").lower().strip() == 'y':
            Config.writeExample("default.cfg")
            log.printV("Example config has been writen, fill it out and relaunch the bot!")
            exit()

    log.printV("Finished checking config.")

    log.setVerbose(cfg['verbose'])

    log.printV("Loading modules...")

    global active_modules
    active_modules = ModuleLoader.loadAll()

    for module in active_modules["Initialize"]:
        module.Initialize()

    log.printV("Modules loaded.")

    log.printV("Activating discord bot...")

    client.run(cfg['token'])


client = discord.Client()

@client.event
async def on_ready():
    log.printV('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    for module in active_modules["TextSend"]:
        await module.TextSend(message, client)


Initilize(client)

