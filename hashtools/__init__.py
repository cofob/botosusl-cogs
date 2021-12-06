from .hashtools import HashTools


def setup(bot):
    bot.add_cog(HashTools(bot))
