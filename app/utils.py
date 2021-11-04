import json

def load_json(path):
    """Load contents from json file."""
    with open(path, "r+", encoding="utf-8") as f:
        return json.loads(f.read())