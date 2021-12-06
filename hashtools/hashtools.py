import hashlib

from redbot.core import commands


class HashTools(commands.Cog):
    """Cog for hashing strings"""

    def __init__(self, bot, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot = bot

    @commands.command()
    async def sha256(self, ctx, *, text: str):
        """SHA256 hash"""
        await ctx.send(hashlib.sha256(text.encode()).hexdigest())
