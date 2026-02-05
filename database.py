# database.py

import json, os

DB_FILE = "database.json"

def _load():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as f:
        return json.load(f)

def _save(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)

# ===== WELCOME =====
def set_welcome(chat_id, text):
    db = _load()
    db.setdefault("welcome", {})[str(chat_id)] = text
    _save(db)

def get_welcome(chat_id):
    return _load().get("welcome", {}).get(str(chat_id))

def del_welcome(chat_id):
    db = _load()
    if "welcome" in db and str(chat_id) in db["welcome"]:
        del db["welcome"][str(chat_id)]
        _save(db)

# ===== FILTER =====
def add_filter(chat_id, word, reply):
    db = _load()
    db.setdefault("filters", {}).setdefault(str(chat_id), {})[word] = reply
    _save(db)

def get_filters(chat_id):
    return _load().get("filters", {}).get(str(chat_id), {})

def del_filter(chat_id, word):
    db = _load()
    try:
        del db["filters"][str(chat_id)][word]
        _save(db)
    except:
        pass
