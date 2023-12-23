import os
from dotenv import load_dotenv

load_dotenv()

PERFECT_DOWNLOAD = os.environ.get("PERFECT_DOWNLOAD")
PERFECT_UPLOAD = os.environ.get("PERFECT_UPLOAD")
PING = os.environ.get("PING")

# telegram
API_TOKEN = os.environ.get("API_TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID")

SLEEP_TIME = os.environ.get("SLEEP_TIME")
