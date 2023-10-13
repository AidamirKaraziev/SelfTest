import os
from dotenv import load_dotenv

load_dotenv()

MIN_DOWNLOAD = os.environ.get("MIN_DOWNLOAD")
MIN_UPLOAD = os.environ.get("MIN_UPLOAD")
PING = os.environ.get("PING")

# telegram
API_TOKEN = os.environ.get("API_TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID")

SLEEP_TIME = os.environ.get("SLEEP_TIME")
