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
        await ctx.send('SHA256 hash:\n```\n'+hashlib.sha256(text.encode()).hexdigest()+'\n```')

    @commands.command()
    async def sha512(self, ctx, *, text: str):
        """SHA512 hash"""
        await ctx.send('SHA512 hash:\n```\n'+hashlib.sha512(text.encode()).hexdigest()+'\n```')

    @commands.command()
    async def sha1(self, ctx, *, text: str):
        """SHA1 hash"""
        await ctx.send('SHA1 hash:\n```\n'+hashlib.sha1(text.encode()).hexdigest()+'\n```')

    @commands.command()
    async def md5(self, ctx, *, text: str):
        """MD5 hash"""
        await ctx.send('MD5 hash:\n```\n'+hashlib.md5(text.encode()).hexdigest()+'\n```')
