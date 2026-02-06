import config
from functools import wraps

def owner_only(func):
    @wraps(func)
    async def wrapper(client, message):
        if message.from_user.id not in config.OWNER_ID:
            return
        return await func(client, message)
    return wrapper
