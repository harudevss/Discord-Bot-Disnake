import os
from disnake import Intents
from disnake.ext.commands import Bot
from config import botPrefix, botToken

class DiscordClient(Bot):
    def __init__(self):
        super().__init__(command_prefix=botPrefix, help_command=None, intents=Intents.all())
    
    def startup(self):
        #Loading Events
        for file in os.listdir("src/events"):
            if file.endswith(".py"):
                self.load_extension(f'src.events.{file[:-3]}')
        #Loading Commands
        for file in os.listdir("src/commands"):
            if file.endswith(".py"):
                self.load_extension(f'src.commands.{file[:-3]}')
        self.run(botToken)