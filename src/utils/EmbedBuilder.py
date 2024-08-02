from disnake import Embed, Member
from config import mainColor

class EmbedBuilder(Embed):
    def __init__(self, title, description, user: Member):
        super().__init__(title=title, description=description, color=mainColor)
        self.set_thumbnail(user.display_avatar)