from discord.ext import commands
from discord.ext import tasks
from dislash import slash_command
import json
import urllib.request
from datetime import datetime
import random


class Slash_haishinCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.among_us = ["<:amoaka:933160923915497492>", "<:amokiiro:935347898546258010>",
                         "<:amomidori:935347876597485608>", "<:amomizu:933161501005611018>"]

    @commands.Cog.listener()
    async def on_ready(self):
        """Cogが読み込まれた時に発動"""
        print('Slash_haishinCog on ready!')

    def haishin(self, ctx):
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
        if streamNum != 0:
            return ('\n'.join(texts))
        else:
            return "公開している配信者はいません"

    @tasks.loop(hours=2)
    async def auto_haishin(self, ctx):
        if self.haishin(ctx) == "公開している配信者はいません":
            pass
        else:
            await ctx.channel.send(self.haishin(ctx))

    @slash_command(name="haishin", description="ぎこぽいぽいで公開している配信を取得します")
    async def slash_haishin(self, ctx):
        await ctx.send(self.haishin(ctx))

    @slash_command(name="starthaishin", description="公開している配信者を2時間ごとに言います")
    async def slash_start_haishin_loop(self, ctx):
        self.auto_haishin.start(ctx)
        await ctx.reply("ok! 配信オートをSTART!")

    @slash_command(name="stophaishin", description="公開している配信者を自動的に言う機能を停止")
    async def slash_stop_haishin_loop(self, ctx):
        self.auto_haishin.stop()
        await ctx.reply("ok! 配信オートをSTOP!")


def setup(bot):
    return bot.add_cog(Slash_haishinCog(bot))
