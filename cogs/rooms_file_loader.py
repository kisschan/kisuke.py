import json


class FileLoader():
    def fileloader():
        try:
            with open(R"cogs/discord_gikopoi2_rooms.json", encoding="utf-8") as f:
                jsn = json.load(f)
                return jsn
        except json.decoder.JSONDecodeError as error:
            print(error)
