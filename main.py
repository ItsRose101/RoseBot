import discord
import commands

# See https://discordpy.readthedocs.io/en/stable/intro.html for info

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('+hello'):
        await message.channel.send('Hello!')


_TOKEN_FILE = open('tokenfile.txt', 'r')
_TOKEN = _TOKEN_FILE.read()
_TOKEN_FILE.close()
client.run(_TOKEN)
