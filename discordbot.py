from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = 'NzAyOTE5MDg2MDY1MTg4OTQ2.XqJ39g.ho6gc9rPgG4ySZlXpLMxX2CmvXU'


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
