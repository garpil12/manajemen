import traceback
import config

async def report_error(client, error):
    if not config.LOG_CHAT:
        return
    text = (
        "🚨 **BOT ERROR**\n\n"
        f"```{error}```"
    )
    await client.send_message(config.LOG_CHAT, text)
