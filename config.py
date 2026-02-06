import os
from dotenv import load_dotenv

load_dotenv()

# ================= TELEGRAM =================
API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

BOT_MODE = os.getenv("BOT_MODE", "userbot")  # userbot | bot
SESSION = os.getenv("SESSION", "manajemen") if BOT_MODE == "userbot" else None

# ================= OWNER & COMMAND =================
OWNER_ID = [int(x) for x in os.getenv("OWNER_ID", "").split() if x]
CMD_PREFIX = os.getenv("CMD_PREFIX", "! . /").split()

# ================= DATABASE =================
DATABASE_URL = os.getenv("DATABASE_URL", "data/database.db")

# ================= LOGGING =================
LOG_CHAT = int(os.getenv("LOG_CHAT")) if os.getenv("LOG_CHAT") else None
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = os.getenv("LOG_FILE", "logs/bot.log")

# ================= SYSTEM =================
TIMEZONE = os.getenv("TIMEZONE", "Asia/Jakarta")
AUTO_RESTART = os.getenv("AUTO_RESTART", "true").lower() == "true"
RESTART_TIME = os.getenv("RESTART_TIME", "00:00")

# ================= SECURITY =================
ANTI_FLOOD = os.getenv("ANTI_FLOOD", "true").lower() == "true"
FLOOD_DELAY = float(os.getenv("FLOOD_DELAY", 1.5))

# ================= VALIDATION =================
if not API_ID or not API_HASH:
    raise RuntimeError("API_ID dan API_HASH WAJIB di set di .env")

if BOT_MODE == "bot" and not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN wajib jika BOT_MODE=bot")

if BOT_MODE not in ("bot", "userbot"):
    raise RuntimeError("BOT_MODE harus 'bot' atau 'userbot'")

# ================= PREPARE DIR =================
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
os.makedirs(os.path.dirname(DATABASE_URL), exist_ok=True)
