from discord.ext import commands  # Bot Commands Frameworkをインポート


class Message_RepeyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_mem = None
        self.among_us = ["<:amoaka:933160923915497492>", "<:amokiiro:935347898546258010>",
                         "<:amomidori:935347876597485608>", "<:amomizu:933161501005611018>"]

    @commands.Cog.listener()
    async def on_ready(self):
        """Cogが読み込まれた時に発動"""
        print('Message_ReplyCog on ready!')

    @commands.command()
    async def ping(self, ctx):
        """動作確認"""
        await ctx.send('おうなんかようか？')

    @commands.command()
    async def name(self, ctx):
        """名前を取得"""
        await ctx.send(ctx.author.display_name)


def setup(bot):
    return bot.add_cog(Message_RepeyCog(bot))
