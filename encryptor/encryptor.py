import base64

from redbot.core import commands


class Encryptor(commands.Cog):
    """Cog for hashing strings"""

    def __init__(self, bot, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot = bot

    @commands.command()
    async def base64(self, ctx, *, text: str):
        """BASE64 text"""
        if text.startswith('b64:'):
            out = 'Decoded BASE64:\n```\n'+base64.b64decode(text[4:]).decode(errors='replace')+'\n```'
        else:
            out = 'BASE64:\n```\nb64:'+base64.b64encode(text.encode()).decode()+'\n```'
        await ctx.send(out)

    @commands.command()
    async def base32(self, ctx, *, text: str):
        """BASE32 text"""
        if text.startswith('b32:'):
            out = 'Decoded BASE32:\n```\n'+base64.b32decode(text[4:]).decode(errors='replace')+'\n```'
        else:
            out = 'BASE32:\n```\nb32:'+base64.b32encode(text.encode()).decode()+'\n```'
        await ctx.send(out)

    @commands.command()
    async def decode(self, ctx, *, text: str):
        """Smart decode"""
        mode = (None, None, None)  # func, name, decode?
        if text.startswith('b64:'):
            mode = (base64.b64decode, 'b', True)
        elif text.startswith('b32:'):
            mode = (base64.b32decode, 'b', True)
        if mode[1] is None:
            return await ctx.send('Cannot find text type!')
        await ctx.send('Decoded text:\n```\n'+(mode[0](text[4:].encode()).decode()
                                               if mode[2] else mode[0](text[4:].encode()))+'\n```')

    @commands.command()
    async def encode(self, ctx, *, text: str):
        """Smart decode"""
        mode = (None, None, None)  # func, name, decode?
        if text.startswith('b64:'):
            mode = (base64.b64encode, 'b', True)
        elif text.startswith('b32:'):
            mode = (base64.b32encode, 'b', True)
        if mode[1] is None:
            return await ctx.send('Cannot find text type!')
        await ctx.send('Encoded text:\n```\n'+(mode[0](text.encode()).decode()
                                               if mode[2] else mode[0](text.encode()))+'\n```')
