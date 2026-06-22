# for testing

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CONFIG_PATH = ROOT / "data" / "camera_config.json"

def load_config():

    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def get_camera_config(camera_id):

    config = load_config()

    return config[camera_id]