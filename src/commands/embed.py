from disnake.ext.commands import Cog, Bot, slash_command
from disnake import Option, OptionType, CommandInteraction
from src import EmbedBuilder

class Embed(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
    
    @slash_command(
            name="embed", 
            description="Send a message which contains Discord Embed feature.",
            options=[
                Option(name="title", description="Enter your title.", required=True),
                Option(name="description", description="Enter your description.", required=True),
            ]
    )
    async def embed(self, inter: CommandInteraction, title, description):
        title = title
        description = description
        user = inter.author
        await inter.response.defer()
        embed = EmbedBuilder(title=str(title), description=(description), user=user)
        await inter.edit_original_message(embed=embed)

def setup(bot: Bot):
    bot.add_cog(Embed(bot))