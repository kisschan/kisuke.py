from discord.ext import commands
from os import getenv
import traceback

# 読み込むCogの名前を格納
INITIAL_EXTENSIONS = [
     'cogs.discord_message_reply'
 ]

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

for cog in INITIAL_EXTENSIONS:
     bot.load_extension(cog)


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
