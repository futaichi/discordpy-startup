import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith("はろー"):
        m = "こんにちは、" + message.author.name + "さん"
        await client.send_message(message.channel,m)

client.run('NzAyOTE5MDg2MDY1MTg4OTQ2.XqP_Yw.rbgQvH4Xs0BiX45r0XNafmhhA18')