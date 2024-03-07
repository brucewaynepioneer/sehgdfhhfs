from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup
from .database.mongo import insert, find_one

@Client.on_message(filters.private & filters.incoming & filters.command("about"))
async def _about(bot, msg):
	id = msg.from_user.id
	ok = find_one(id)
	if ok:
		await bot.send_message(
			msg.chat.id,
			"**Best Telegram Bot to generate string... **\n" + Data.ABOUT,
			reply_markup=InlineKeyboardMarkup(Data.home_buttons)
		)
	else:
		insert(id)
		await msg.reply_text(
			text=Data.ABOUT, 
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(Data.home_buttons)
		) 

@Client.on_message(filters.private & filters.incoming & filters.command("help"))
async def _help(bot, msg):
	id = msg.from_user.id
	ok = find_one(id)
	if ok:
		await bot.send_message(
			msg.chat.id,
			"**Best Telegram Bot to generate string...**\n" + Data.HELP,
			reply_markup=InlineKeyboardMarkup(Data.home_buttons)
		)
	else:
		insert(id)
		await msg.reply_text(
			text=Data.HELP, 
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(Data.home_buttons)
		) 


# Assuming you have defined the video path somewhere in your code
VIDEO_PATH = "start.mp4"

@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def _start(bot, msg):
    user_id = msg.from_user.id
    # Assuming `find_one` and `insert` functions are defined elsewhere
    ok = find_one(user_id)
    if ok:
        await bot.send_animation(
            chat_id=msg.chat.id,
            animation=VIDEO_PATH,
            caption="This is an advanced Pyrogram and Telethon string session generator bot made with ❤️ by __**[Team SPY](https://t.me/dev_gagan)**__.",
            reply_markup=InlineKeyboardMarkup(Data.home_buttons)
        )
    else:
        insert(user_id)
        # Send the video with the welcome text and buttons
        await bot.send_animation(
            chat_id=msg.chat.id,
            animation=VIDEO_PATH,
            caption="This is an advanced Pyrogram and Telethon string session generator bot made with ❤️ by __**[Team SPY](https://t.me/dev_gagan)**__.",
            reply_markup=InlineKeyboardMarkup(Data.home_buttons)
        )
