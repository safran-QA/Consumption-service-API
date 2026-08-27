import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "test_data.json"


def save_data(key, value):
    data = {}

    if DATA_FILE.exists():
        try:
            data = json.loads(DATA_FILE.read_text())
        except json.JSONDecodeError:
            data = {}

    data[key] = value
    DATA_FILE.write_text(json.dumps(data, indent=2))


def get_data(key, default=None):
    if not DATA_FILE.exists():
        return default

    try:
        data = json.loads(DATA_FILE.read_text())
    except json.JSONDecodeError:
        return default

    return data.get(key, default)


def get_all_data():
    if not DATA_FILE.exists():
        return {}

    try:
        return json.loads(DATA_FILE.read_text())
    except json.JSONDecodeError:
        return {}
