# PRE PROCESSING --------------------------------------------------------
import subprocess

# Dependency guards
try:
    import discord
except ImportError:
    print("Discord.py failed to load, installing it now.")
    subprocess.run("pip","install","discord.py")
    exit(0x01)
try:
    from discord.ext import commands, tasks
except ImportError:
    print("Fatal failure to load discord extensions. Discord.py failed to install. Install it and try again.")
    exit(0x01)
try:
    import os
except ImportError:
    print("Fatal failure to load system module. I don't know how this could possibly happen...")
    exit(0x01)

# -----------------------------------------------------------------------

PREFIX = '+'
bot = discord.ext.commands.Bot(command_prefix=PREFIX) # See https://discordpy.readthedocs.io/en/stable/intro.html for info
# This variable (PREFIX) is the symbol that every command starts with, like the '!' for Rythm bot.

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

# LOAD PROCESSING --------------------------------------------------------
@bot.command()
@commands.dm_only()
async def reload(ctx, *, name: str):
    try:
        bot.reload_extension(f"cogs.{name}")
    except Exception as e:
        return await ctx.send(e)
    await ctx.send(f'"**{name}**" Cog reloaded')

@bot.command()
@commands.dm_only()
async def unload(ctx, *, name: str):
    try:
        bot.unload_extension(f"cogs.{name}")
    except Exception as e:
        return await ctx.send(e)
    await ctx.send(f'"**{name}**" Cog unloaded')

@bot.command()
@commands.dm_only()
async def load(ctx, *, name: str):
    try:
        bot.load_extension(f"cogs.{name}")
    except Exception as e:
        return await ctx.send(e)
    await ctx.send(f'"**{name}**" Cog loaded')

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        name = file[:-3] 
        bot.load_extension(f"cogs.{name}")

# -----------------------------------------------------------------------

# TOKEN LOGIN
_TOKEN_FILE = open('tokenfile.txt', 'r')
_TOKEN = _TOKEN_FILE.read()
_TOKEN_FILE.close()

# LOGIN
bot.run(_TOKEN)