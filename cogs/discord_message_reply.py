from discord.ext import commands  # Bot Commands Frameworkをインポート
import json
import urllib.request
from datetime import datetime
import random


class Message_RepeyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
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
        await ctx.send(f'{ctx.author.name}はくさぃ・・・')

    @commands.command()
    async def 配信(self, ctx):
        """ぎこぽいの配信者を取得。部屋まで飛べる"""
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
        await ctx.send(('\n'.join(texts)))


def setup(bot):
    return bot.add_cog(Message_RepeyCog(bot))
