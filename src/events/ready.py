from disnake.ext.commands import Cog, Bot

class Ready(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
    
    @Cog.listener()
    async def on_ready(self):
        print(f"Bot is online: {self.bot.user.name}")

def setup(bot: Bot):
    bot.add_cog(Ready(bot))