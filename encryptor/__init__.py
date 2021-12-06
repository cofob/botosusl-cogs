from .encryptor import Encryptor


def setup(bot):
    bot.add_cog(Encryptor(bot))
