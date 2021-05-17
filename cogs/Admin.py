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

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}.'.format(member))
    
    # ALL ADMIN COMMANDS GO IN HERE AS FUNCTIONS --------------------------
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Latency: {round(self.bot.latency * 1000)} ms")

    @commands.command()
    async def argcheck(self, ctx, *args):
        await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))

    # ---------------------------------------------------------------------

    @commands.Cog.listener()
    async def on_ready(self):
        print("Admin commands readied.")

def setup(bot):
    bot.add_cog(Admin(bot))