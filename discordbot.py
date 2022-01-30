from discord.ext import commands
from discord.ext.commands import CommandNotFound
from os import getenv
import traceback

bot = commands.Bot(command_prefix='')
bot.load_extension("cogs.discord_message_reply")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

token = getenv('DISCORD_BOT_TOKEN')
bot.run('ODU5NDI3OTUwNzIwOTc0ODQ5.YNsipg.M3nT7oPNcyTkmbsbDEek7IXEE88')
