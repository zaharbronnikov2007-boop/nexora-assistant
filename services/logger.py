import json
from pathlib import Path

DATA_DIR = Path("data")


def _read(filename):
    path = DATA_DIR / filename

    if not path.exists():
        return []

    with open(path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return []


def _write(filename, data):
    path = DATA_DIR / filename

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def log_user(user):
    users = _read("users.json")

    if any(x["id"] == user.id for x in users):
        return

    users.append({
        "id": user.id,
        "name": user.full_name,
        "username": user.username,
    })

    _write("users.json", users)


def log_ai(user):
    ai = _read("ai.json")

    ai.append({
        "id": user.id,
        "name": user.full_name,
    })

    _write("ai.json", ai)


def log_calculator(user):
    calc = _read("calculator.json")

    calc.append({
        "id": user.id,
        "name": user.full_name,
    })

    _write("calculator.json", calc)


def log_lead(data):
    leads = _read("leads.json")

    leads.append(data)

    _write("leads.json", leads)


def stats():
    return {
        "users": len(_read("users.json")),
        "ai": len(_read("ai.json")),
        "calculator": len(_read("calculator.json")),
        "leads": len(_read("leads.json")),
    }