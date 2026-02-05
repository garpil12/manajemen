# moduls/help.py

from pyrogram import Client, filters

HELP = {
    "admin": "• ban\n• kick\n• mute",
    "welcome": "• savwel\n• rmwel",
    "filter": "• addfilter\n• delfilter",
    "info": "• ping\n• uptime",
    "broadcast": "• broadcast",
}

@Client.on_message(filters.command("help"))
async def help_cmd(client, message):
    text = "**📚 MENU BOT**\n\n"
    for k, v in HELP.items():
        text += f"**{k.upper()}**\n{v}\n\n"
    await message.reply(text)
