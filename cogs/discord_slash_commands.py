from discord.ext import commands
from dislash import slash_command, Option, OptionChoice
from .rooms_file_loader import FileLoader

gikopoipoigen = "https://gikopoipoi.net/?areaid=gen&roomid="

roomid = FileLoader.fileloader()


class Slash_haishinCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_ready(self):
        """Cogが読み込まれた時に発動"""
        print("discord_slash_commands.py on ready!")

    @slash_command(name="gikopoipoi",
                   description="gikopoipoiのURLを貼る(仕様上バーまで）",
                   options=[
                       Option("rooms_bar",
                              "ぎこぽいぽいのURLを貼る(バーまで)",
                              3,
                              True,
                              [
                                  OptionChoice('井戸A', gikopoipoigen + roomid['井戸A']),
                                  OptionChoice('井戸B', gikopoipoigen + roomid['井戸B']),
                                  OptionChoice('鰻道', gikopoipoigen + roomid['鰻道']),
                                  OptionChoice('宴会', gikopoipoigen + roomid['宴会']),
                                  OptionChoice('海岸', gikopoipoigen + roomid['海岸']),
                                  OptionChoice('開発局', gikopoipoigen + roomid['開発局']),
                                  OptionChoice('開発局通り', gikopoipoigen + roomid['開発局通り']),
                                  OptionChoice('学校 教室', gikopoipoigen + roomid['学校 教室']),
                                  OptionChoice('学校 校庭', gikopoipoigen + roomid['学校 校庭']),
                                  OptionChoice('学校 国際教室', gikopoipoigen + roomid['学校 国際教室']),
                                  OptionChoice('学校 パソコンルーム', gikopoipoigen + roomid['学校 パソコンルーム']),
                                  OptionChoice('学校 廊下', gikopoipoigen + roomid['学校 廊下']),
                                  OptionChoice('学校通り', gikopoipoigen + roomid['学校通り']),
                                  OptionChoice('カフェ通り', gikopoipoigen + roomid['カフェ通り']),
                                  OptionChoice('コンビニ', gikopoipoigen + roomid['コンビニ']),
                                  OptionChoice('サイロ', gikopoipoigen + roomid['サイロ']),
                                  OptionChoice('神社', gikopoipoigen + roomid['神社']),
                                  OptionChoice('神社入り口', gikopoipoigen + roomid['神社入り口']),
                                  OptionChoice('高台', gikopoipoigen + roomid['高台']),
                                  OptionChoice('高台の階段', gikopoipoigen + roomid['高台の階段']),
                                  OptionChoice('地下街', gikopoipoigen + roomid['地下街']),
                                  OptionChoice('地下街 居酒屋 名無し', gikopoipoigen + roomid['地下街 居酒屋 名無し']),
                                  OptionChoice('地下街 バー774', gikopoipoigen + roomid['地下街 バー774']),
                                  OptionChoice('電車', gikopoipoigen + roomid['電車']),
                                  OptionChoice('バー', gikopoipoigen + roomid['バー'])
                              ])
                   ])
    async def gikopoipoi(self, inter, rooms_bar):
        await inter.reply(rooms_bar)

    @slash_command(name="gikopoipoi2",
                   description="gikopoipoiのURLを貼る(バーから)",
                   options=[
                       Option("bar_rooms", "gikopoipoiのURLを貼る(バーから)", 3, True,
                              [
                                  OptionChoice('ＢＡＲギコ', gikopoipoigen + roomid['ＢＡＲギコ']),
                                  OptionChoice('ＢＡＲギコ 下階', gikopoipoigen + roomid['ＢＡＲギコ 下階']),
                                  OptionChoice('バー通り', gikopoipoigen + roomid['バー通り']),
                                  OptionChoice('バス停', gikopoipoigen + roomid['バス停']),
                                  OptionChoice('ハッカーのアジト', gikopoipoigen + roomid['ハッカーのアジト']),
                                  OptionChoice('秘密のバー', gikopoipoigen + roomid['秘密のバー']),
                                  OptionChoice('噴水広場', gikopoipoigen + roomid['噴水広場']),
                                  OptionChoice('もなちゃと', gikopoipoigen + roomid['もなちゃと']),
                                  OptionChoice('屋台', gikopoipoigen + roomid['屋台']),
                                  OptionChoice('吉野家', gikopoipoigen + roomid['吉野家']),
                                  OptionChoice('ラヂヲ局', gikopoipoigen + roomid['ラヂヲ局']),
                                  OptionChoice('ラヂヲ局 楽屋', gikopoipoigen + roomid['ラヂヲ局 楽屋']),
                                  OptionChoice('ラヂヲ局 第1スタジオ', gikopoipoigen + roomid['ラヂヲ局 第1スタジオ']),
                                  OptionChoice('ラヂヲ局 第2スタジオ BEAT GIKO', gikopoipoigen + roomid['ラヂヲ局 第2スタジオ BEAT GIKO']),
                                  OptionChoice('ラヂヲ局 第3スタジオ G-SQUID', gikopoipoigen + roomid['ラヂヲ局 第3スタジオ G-SQUID']),
                                  OptionChoice('ラヂヲ局 舞台裏', gikopoipoigen + roomid['ラヂヲ局 舞台裏']),
                              ]
                              )
                   ]
                   )
    async def gikopoipoi2(self, inter, bar_rooms):
        await inter.reply(bar_rooms)


def setup(bot):
    return bot.add_cog(Slash_haishinCog(bot))
