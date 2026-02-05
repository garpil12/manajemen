# main.py

from pyrogram import Client
import config
import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format="%(name)s - %(levelname)s - %(message)s"
)

app = Client(
    name=config.SESSION,
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

# auto load semua modul
def load_modules():
    for file in os.listdir("moduls"):
        if file.endswith(".py") and not file.startswith("_"):
            __import__(f"moduls.{file[:-3]}")

@app.on_message()
async def _():
    pass

if __name__ == "__main__":
    load_modules()
    print("🔥 BOT MANJEMEN AKTIF")
    app.run()
