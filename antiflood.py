import time
from collections import defaultdict

FLOOD_LIMIT = 5   # pesan
FLOOD_TIME = 4    # detik

users = defaultdict(list)

def is_flood(user_id):
    now = time.time()
    users[user_id] = [t for t in users[user_id] if now - t < FLOOD_TIME]
    users[user_id].append(now)
    return len(users[user_id]) > FLOOD_LIMIT
