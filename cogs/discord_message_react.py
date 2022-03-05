from discord.ext import commands
import re
import json
import urllib.request
from datetime import datetime
import random
import time


class Message_ReactCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.among_us = ["<:amoaka:933160923915497492>", "<:amokiiro:935347898546258010>",
                         "<:amomidori:935347876597485608>", "<:amomizu:933161501005611018>"]
        self.switch_haishin = False

    @commands.Cog.listener()
    async def on_ready(self):
        """Cogが読み込まれた時に発動"""
        print('Message_ReactCog on ready!')

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.content == "配信":
            self.switch_haishin = True
            while self.switch_haishin is True:
                streamer_emoji = ["👩", "👱", "👨", "👧"]
                if ctx.guild.id == 930151110335938640:
                    streamer_emoji = self.among_us
                texts = ['http://gikopoipoi.net  で配信中']
                texts.extend([datetime.now().strftime('%Y{0}%-m{1}%-d{2} %-H{3}%-M{4}%-S{5}').format(*'年月日時分秒')])
                url = 'https://gikopoipoi.net/areas/gen/streamers'
                req = urllib.request.Request(url)
                streamNum = 0
                randomEmoji = []
                with urllib.request.urlopen(req) as res:
                    body = json.load(res)
                for item in body:
                    streamNum = streamNum + len(item['streamers'])
                    texts.extend([i if i else '名無しさん' for i in item['streamers']])
                    texts.extend(['https://gikopoipoi.net/?areaid=gen&roomid=' + item['id']])
                for item in range(streamNum):
                    randomEmoji.extend([random.choice(streamer_emoji)])
                texts.insert(2, "(" + str(streamNum) + "名が配信中)")
                texts.insert(2, ''.join(randomEmoji))
                time.sleep(1*60*60*1)
                await ctx.channel.send(('\n'.join(texts)))
        if ctx.content == "配信おわり":
            self.switch_haishin = False
        if ctx.author.bot:
            return
        if re.search("(?:([こコｺ][ろロﾛ]|殺)[すスｽ]|koro?su)|([死氏市四４4しシｼ][ねネﾈ][よヨょョﾖｮ]?)", ctx.content):
            await ctx.delete()
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
