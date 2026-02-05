# logger.py

import logging
import os
from logging.handlers import RotatingFileHandler

LOG_DIR = "logs"
LOG_FILE = "bot.log"

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def setup_logger(name="BOT"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # cegah duplicate log
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # log ke file (auto rotate)
    file_handler = RotatingFileHandler(
        os.path.join(LOG_DIR, LOG_FILE),
        maxBytes=2 * 1024 * 1024,  # 2MB
        backupCount=3
    )
    file_handler.setFormatter(formatter)

    # log ke console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
