import asyncio
import datetime
import os
import sys
import config
from logger import setup_logger

log = setup_logger("SCHEDULER")

async def auto_restart():
    if not config.AUTO_RESTART:
        return

    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == config.RESTART_TIME:
            log.warning("⏰ Auto restart triggered")
            await asyncio.sleep(2)
            os.execv(sys.executable, [sys.executable] + sys.argv)

        await asyncio.sleep(30)
