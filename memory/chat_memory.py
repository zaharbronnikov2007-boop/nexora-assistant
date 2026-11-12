from collections import defaultdict

MAX_HISTORY = 10

_history = defaultdict(list)


def add_message(user_id: int, role: str, content: str):
    _history[user_id].append(
        {
            "role": role,
            "content": content,
        }
    )

    if len(_history[user_id]) > MAX_HISTORY:
        _history[user_id] = _history[user_id][-MAX_HISTORY:]


def get_history(user_id: int):
    return list(_history[user_id])


def clear_history(user_id: int):
    _history[user_id].clear()
    