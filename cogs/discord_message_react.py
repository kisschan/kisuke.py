from discord.ext import commands
import re


class Message_ReactCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.among_us = ["<:amoaka:933160923915497492>", "<:amokiiro:935347898546258010>",
                         "<:amomidori:935347876597485608>", "<:amomizu:933161501005611018>"]

    @commands.Cog.listener()
    async def on_ready(self):
        """Cogが読み込まれた時に発動"""
        print('Message_ReactCog on ready!')

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author.bot:
            return
        if re.search("(?:([おオｵ][めメメ][でデﾃﾞ][とトﾄ]?[うウｳ]?)|([やヤﾔ][っッｯ][たタﾀ][ーｰ]))", ctx.content):
            congratulation = ["🎉", "🎊", "㊗️"]
            for item in congratulation:
                await ctx.add_reaction(item)

        if re.search(r"(?:([あアｱ][もモﾓ][んンﾝ]?[ぐグｸﾞ]?[あアｱ][すスｽ]|(?i:among\s?us)))", ctx.content):
            await ctx.add_reaction("🎮")
            if ctx.guild.id == 930151110335938640:
                for item in self.among_us:
                    await ctx.add_reaction(item)
        if re.search(r"(?:(([まマﾏ][ーｰあアｱ]|麻)(([じジ]|ｼﾞ)[ゃャｬ][んンﾝ]|雀)))", ctx.content):
            await ctx.add_reaction("🀄")
        if re.search(r"(?:(([ぱパ]|ﾊﾟ)([ずズ]|ｽﾞ)[るルﾙ]))", ctx.content):
            await ctx.add_reaction("🧩")
        if re.search(r"(?:([のノﾉ飲][みミﾐ]|[酒]|([びビ]|ﾋﾞ)[ーｰい][るルﾙ]))", ctx.content):
            await ctx.add_reaction("🍻")
        if re.search(r"(?:([たタﾀ]([ばバ]|ﾊﾞ)[こコｺ]|[しシｼ][ーｰ][しシｼ][ゃャｬ]))", ctx.content):
            await ctx.add_reaction("🚬")
        if re.search(r"(?:([いイｲ]([いイｲ]|[ーｰ])[ねネﾈ]))", ctx.content):
            await ctx.add_reaction("👍🏻")

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if re.search("(?:([こコｺ][ろロﾛ]|殺)[すスｽ]|koro?su)|([死氏４4しシｼ][ねネﾈ][よヨょョﾖｮ]?)", after.content):
            await after.delete()


def setup(bot):
    return bot.add_cog(Message_ReactCog(bot))
