from discord.ext import commands  # Bot Commands Frameworkをインポート
import discord

    class Message_RepeyCog(commands.Cog):
        def __init__(self, bot):
            self.bot = bot
            self._last_member = None
 
        @commands.Cog.listener()
        # Cogが読み込まれた時に発動
        async def on_ready(self):
            print('Message_RepeyCog on ready!')
 
        @bot.command()
        async def ping(ctx):
            await ctx.send('おうなんかようか？')

        @bot.command()
        async def 竜介(ctx):
            await ctx.send('くさい　だろぅな・・')
 
    def setup(bot):
    bot.add_cog(Message_RepeyCog(bot)) # Message_RepeyCogにBotを渡してインスタンス化し、Botにコグとして登録する