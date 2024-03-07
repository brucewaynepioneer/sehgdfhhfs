from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

I can generate pyrogram and telethon string session . 
Use the below button and go ahead !

By @dev_gagan
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("Start Generating Session", callback_data="generate")],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("Start Generating Session...", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("Start Generating Session...", callback_data="generate")],
        [InlineKeyboardButton(" Visit Site ⭐", url="https://devgagan.in")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton(" Get Help ↗️", url="https://t.me/dev_gagan")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - About The Bot
/help - To display current Message
/start - Start the Bot
/generate - Generate String Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    # About Message
    ABOUT = """
**About This Bot**

A telegram bot to generate pyrogram and telethon string session by @dev_gagan

GitHub : [Click Here](https://github.com/devgaganin)
Framework : [Pyrogram](docs.pyrogram.org)
Language : [Python](www.python.org)
Developer : @dev_gagan
    """
