try:
    import discord
except ImportError:
    print("Discord.py failed to load, install it now.")
    exit(0x01)
try:
    from discord.ext import commands, tasks
except ImportError:
    print("Fatal failure to load discord extensions. Discord.py failed to install. Install it and try again.")
    exit(0x01)

class Anime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # ALL ANIME COMMANDS GO IN HERE AS FUNCTIONS --------------------------

    # I will condense these into a gif command at some point
    @commands.command()
    async def deku(self, ctx):
        await ctx.send("https://tenor.com/view/anime-headbang-gif-6035620")

    @commands.command()
    async def hehehe(self, ctx):
        await ctx.send("https://tenor.com/view/naruto-smile-gif-5677612")

    @commands.command()
    async def sob(self, ctx):
        await ctx.send("https://tenor.com/view/umaru-san-cry-tears-sad-sob-gif-5086387")
    # ---------------------------------------------------------------------

    @commands.Cog.listener()
    async def on_ready(self):
        print("Anime commands readied.")

def setup(bot):
    bot.add_cog(Anime(bot))

