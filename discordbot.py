


import discord
import asyncio

client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']



@client.event
async def on_message(message):
    if message.content.startswith("はろー"):
        m = "こんにちは、" + message.author.name + "さん"
        await client.send_message(message.channel,m)

client.run('token')
