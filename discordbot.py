from discord.ext import commands
from discord.ext.commands import CommandNotFound
from dislash import slash_commands
from os import getenv
import traceback

bot = commands.Bot(command_prefix='')
client = commands.Bot(command_prefix='/')
slash = slash_commands.InteractionClient(bot, test_guilds=[932885441693220914, 889154286028738611, 930151110335938640, 961729817529704568])

bot.load_extension("cogs.discord_message_reply")
bot.load_extension("cogs.discord_message_react")
bot.load_extension("cogs.discord_slash_commands")


@slash.slash_command(name="ping", description="動作確認")
async def hello(inter):
    await inter.respond("hi this is 配信BOT ver0.11")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
