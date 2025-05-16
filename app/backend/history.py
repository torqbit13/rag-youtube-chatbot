import os

from backend.config import CHAT_HISTORY_FILE


def load_chat_history():
    if not os.path.exists(CHAT_HISTORY_FILE):
        return []
    with open(CHAT_HISTORY_FILE, "r") as f:
        try:
            return [eval(line.strip()) for line in f.readlines()]
        except Exception:
            return []


def save_chat_history(history):
    with open(CHAT_HISTORY_FILE, "w") as f:
        for msg in history:
            f.write(f"{repr(msg)}\n")


def clear_chat_history():
    open(CHAT_HISTORY_FILE, "w").close()
