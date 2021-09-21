from discord.ext import commands  # Bot Commands Frameworkをインポート

class Message_RepeyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    # Cogが読み込まれた時に発動
    async def on_ready(self):
        print('Message_RepeyCog on ready!')

    @commands.command()
    async def ping(self,ctx):
        await ctx.send('おうなんかようか？')

    @commands.command()
    async def 竜介(self,ctx):
        await ctx.send('くさい　だろぅな・・')

    def setup(bot):
        return bot.add_cog(Message_RepeyCog(bot))