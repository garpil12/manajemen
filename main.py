# main.py
import os
import sys
import signal
import importlib
import platform
from pyrogram import Client, filters

import config
from logger import setup_logger
from antiflood import is_flood
from error_handler import register_error_handler

# ================= LOGGER =================
log = setup_logger("MAIN")

# ================= VALIDATE CONFIG =================
REQUIRED_CONFIG = ["API_ID", "API_HASH", "BOT_TOKEN", "SESSION"]

for key in REQUIRED_CONFIG:
    if not hasattr(config, key):
        raise RuntimeError(f"[CONFIG ERROR] {key} belum di set di config.py")

# ================= CLIENT =================
app = Client(
    name=config.SESSION,
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

# ================= LOAD MODULES =================
def load_modules():
    base = "modules"
    total = 0

    if not os.path.isdir(base):
        log.error("Folder modules/ tidak ditemukan!")
        return

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

# ================= GLOBAL ANTIFLOOD =================
@app.on_message(filters.text & ~filters.service)
async def global_antiflood(client, message):
    try:
        if message.from_user and is_flood(message.from_user.id):
            await message.delete()
            log.warning(
                f"Flood blocked | user={message.from_user.id} "
                f"chat={message.chat.id}"
            )
    except Exception:
        pass

# ================= GRACEFUL SHUTDOWN =================
def shutdown_handler(sig, frame):
    log.warning(f"Shutdown signal received: {sig}")
    try:
        app.stop()
    finally:
        sys.exit(0)

signal.signal(signal.SIGINT, shutdown_handler)
signal.signal(signal.SIGTERM, shutdown_handler)

# ================= START BOT =================
if __name__ == "__main__":
    try:
        log.info("======================================")
        log.info("🚀 BOT MANAJEMEN STARTING")
        log.info(f"Python      : {platform.python_version()}")
        log.info(f"OS          : {platform.system()} {platform.release()}")
        log.info(f"PID         : {os.getpid()}")
        log.info("======================================")

        load_modules()
        register_error_handler(app)

        app.run()

    except KeyboardInterrupt:
        log.warning("Bot dihentikan manual (CTRL+C)")

    except Exception as e:
        log.critical("🔥 BOT CRASH !!!")
        log.exception(e)
        sys.exit(1)
