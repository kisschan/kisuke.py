from discord.ext import commands  # Bot Commands Frameworkをインポート
import json
import urllib.request
from datetime import datetime

class Message_RepeyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    # Cogが読み込まれた時に発動
    async def on_ready(self):
        print('Message_RepeyCog on ready!')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('おうなんかようか？')

    @commands.command()
    async def 竜介(self, ctx):
        await ctx.send('くさい　だろぅな・・')

    @commands.command()
    async def name(self, ctx):
        await ctx.send(f'{ctx.author.name}はくさぃ・・・')

    @commands.command()
    async def 配信(self, ctx):
        texts = ['http://gikopoipoi.net  で配信中']
        url = 'https://gikopoipoi.net/areas/gen/streamers'
        texts.extend([datetime.now().strftime('%Y{0}%-m{1}%-d{2} %-H{3}%-M{4}%-S{5}').format(*'年月日時分秒')])
        texts.extend(["-"])
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as res:
            body = json.load(res)
        for item in body:
            texts.extend([i if i else '名無しさん' for i in item['streamers']])
            texts.extend(['https://gikopoipoi.net/?areaid=gen&roomid=' + j for j in item['id']])
        await ctx.send(('\n'.join(texts)))

def setup(bot):
    return bot.add_cog(Message_RepeyCog(bot))
