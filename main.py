from pyrogram import Client, idle
from configs import Config
from pyromod import listen
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

Gagan = Client(
    "Bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="Gagan"),
)

if __name__ == "__main__":
    try:
        Gagan.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    bot = Gagan.get_me().username
    print(f"@{bot} Started Successfully!")
    idle()
    Gagan.stop()
    print("Bot Stopped!")
