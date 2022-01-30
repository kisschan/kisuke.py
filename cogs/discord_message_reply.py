from discord.ext import commands  # Bot Commands Frameworkをインポート
import json
import urllib.request
from datetime import datetime
import re

class Message_RepeyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_ready(self):
        """Cogが読み込まれた時に発動"""
        print('Message_RepeyCog on ready!')

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
        texts = ['http://gikopoipoi.net  で配信中']
        texts.extend([datetime.now().strftime('%Y{0}%-m{1}%-d{2} %-H{3}%-M{4}%-S{5}').format(*'年月日時分秒')])
        streamNum = 0
        url = 'https://gikopoipoi.net/areas/gen/streamers'
        texts.extend(["-"])
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as res:
            body = json.load(res)
        for item in body:
            streamNum = streamNum + len(item['streamers'])
            texts.extend([i if i else '名無しさん' for i in item['streamers']])
            texts.extend(['https://gikopoipoi.net/?areaid=gen&roomid=' + item['id']])
        texts.insert(2, "(" + str(streamNum) + "名が配信中)")
        await ctx.send(('\n'.join(texts)))

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author.bot:
            return
        if re.search("(?:([こコｺ][ろロﾛ]|殺)[すスｽ]|koro?su)|([死氏市四４4しシｼ][ねネﾈ][よヨょョﾖｮ]?)", ctx.content):
            await ctx.delete()
        if re.search("(?:([おオｵ][めメメ][でデﾃﾞ][とトﾄ]?[うウｳ]?)|([やヤﾔ][っッｯ][たタﾀ]))", ctx.content):
            congratulation = ["🎉", "🎊", "㊗️"]
            for item in congratulation:
                await ctx.add_reaction(item)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if re.search("(?:([こコｺ][ろロﾛ]|殺)[すスｽ]|koro?su)|([死氏市四４4しシｼ][ねネﾈ][よヨょョﾖｮ]?)", after.content):
            await after.delete()

def setup(bot):
    return bot.add_cog(Message_RepeyCog(bot))
