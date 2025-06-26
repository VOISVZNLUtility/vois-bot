import json

def get_current_version():
    try:
        with open("version_history.json", "r") as f:
            history = json.load(f)
        return history[-1]["version"]
    except:
        return "v0.0.0"