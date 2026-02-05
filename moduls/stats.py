from pyrogram import Client, filters
import psutil, time, os

START_TIME = time.time()

def uptime():
    t = int(time.time() - START_TIME)
    h, m, s = t // 3600, (t % 3600) // 60, t % 60
    return f"{h}h {m}m {s}s"

@Client.on_message(filters.command("stats"))
async def stats_cmd(client, message):
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    await message.reply(
        f"📊 **BOT STATS**\n\n"
        f"🖥 CPU: `{cpu}%`\n"
        f"💾 RAM: `{ram}%`\n"
        f"📂 DISK: `{disk}%`\n"
        f"⏱ UPTIME: `{uptime()}`"
    )
