# main.py

import os
import sys
import importlib
from pyrogram import Client, filters

import config
from logger import setup_logger
from antiflood import is_flood

# ================= LOGGER =================
log = setup_logger("MAIN")

# ================= CLIENT =================
app = Client(
    name=config.SESSION,
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

# ================= LOAD MODULS =================
def load_modules():
    base = "moduls"
    total = 0

    for file in os.listdir(base):
        if file.endswith(".py") and not file.startswith("_"):
            module = f"{base}.{file[:-3]}"
            try:
                importlib.import_module(module)
                log.info(f"Loaded module: {module}")
                total += 1
            except Exception as e:
                log.error(f"Failed loading module: {module}")
                log.exception(e)

    log.info(f"Total modules loaded: {total}")

# ================= ANTI FLOOD GLOBAL =================
@app.on_message(filters.text & ~filters.edited)
async def global_antiflood(client, message):
    try:
        if message.from_user and is_flood(message.from_user.id):
            await message.delete()
            log.warning(
                f"Flood blocked | user={message.from_user.id} "
                f"chat={message.chat.id}"
            )
    except:
        pass

# ================= START BOT =================
if __name__ == "__main__":
    try:
        load_modules()
        log.info("🚀 BOT MANAJEMEN STARTING...")
        app.run()
    except KeyboardInterrupt:
        log.warning("Bot dihentikan manual")
    except Exception as e:
        log.critical("BOT CRASH !!!")
        log.exception(e)
        sys.exit(1)
