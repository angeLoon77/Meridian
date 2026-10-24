import os
import json
from platformdirs import user_data_dir

folder = user_data_dir(appname="Meridian", appauthor="angeLoon DEV")
os.makedirs(folder, exist_ok=True)
extracted_data = os.path.join(folder, "stocks_data.json")

def load_data(path):
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return {}

def save_data(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)