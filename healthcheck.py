import os
import sys

if os.path.exists("bot_running.flag"):
    sys.exit(0)
else:
    sys.exit(1)
