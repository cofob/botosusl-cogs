import base64

from Crypto.Cipher import AES

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
            out = 'Decoded BASE64:\n```\n' + base64.b64decode(text[4:]).decode(errors='replace') + '\n```'
        else:
            out = 'BASE64:\n```\nb64:' + base64.b64encode(text.encode()).decode() + '\n```'
        await ctx.send(out)

    @commands.command()
    async def base32(self, ctx, *, text: str):
        """BASE32 text"""
        if text.startswith('b32:'):
            out = 'Decoded BASE32:\n```\n' + base64.b32decode(text[4:]).decode(errors='replace') + '\n```'
        else:
            out = 'BASE32:\n```\nb32:' + base64.b32encode(text.encode()).decode() + '\n```'
        await ctx.send(out)

    @commands.command()
    async def aes(self, ctx, key, text: str):
        """AES256 and BASE64 given text with key
            :param text
            BASE64 encoded text
        """
        key = key.encode()
        if len(key) < 16:
            key = key + (b'0' * (16-len(key)))
        if len(key) > 16:
            key = key[:16]
        if text.startswith('aes:'):
            try:
                lst = text.split(':')
                nonce = base64.b64decode(lst[1])
                tag = base64.b64decode(lst[2])
                ciphertext = base64.b64decode(lst[3])
                cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
                plaintext = cipher.decrypt(ciphertext)
                try:
                    cipher.verify(tag)
                except ValueError:
                    return await ctx.send('Message failed tag verification')
            except Exception as e:
                return await ctx.send('Message format invalid ' + str(e))
            out = 'BASE64:\n```\n' + base64.b64encode(plaintext).decode() + '\n```'
        elif text.startswith('b64:'):
            cipher = AES.new(key, AES.MODE_EAX)
            nonce = cipher.nonce
            ciphertext, tag = cipher.encrypt_and_digest(base64.b64decode(text[4:]))
            out = 'AES256:\n```\naes:' + base64.b64encode(nonce).decode() + ':' \
                  + base64.b64encode(tag).decode() + ':' \
                  + base64.b64encode(ciphertext).decode() + '\n```'
        else:
            return await ctx.send('Message text must be in base64!')
        await ctx.send(out)

    @commands.command()
    async def decode(self, ctx, *, text: str):
        """Smart decode"""
        mode = (None, None, None)  # func, name, decode?
        if text.startswith('b64:'):
            mode = (base64.b64decode, 'b64', True)
        elif text.startswith('b32:'):
            mode = (base64.b32decode, 'b32', True)
        if mode[1] is None:
            return await ctx.send('Cannot find text type!')
        await ctx.send('Decoded text:\n```\n' + (mode[0](text[4:].encode()).decode()
                                                 if mode[2] else mode[0](text[4:].encode())) + '\n```')

    @commands.command()
    async def encode(self, ctx, *, text: str):
        """Smart encode"""
        mode = (None, None, None)  # func, name, decode?
        if text.startswith('b32:'):
            mode = (base64.b32encode, 'b32', True)
        elif text.startswith('b64:'):
            mode = (base64.b64encode, 'b64', True)
        if mode[1] is None:
            return await ctx.send('Cannot find text type!')
        await ctx.send('Encoded text:\n```\n' + mode[1] + ':' + (mode[0](text[4:].encode()).decode()
                                                                 if mode[2] else mode[0](text[4:].encode())) + '\n```')
