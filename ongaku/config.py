# config.py

import os
import dotenv

if os.path.isfile("config.env"):
    dotenv.load_dotenv("config.env")


class Config:

    API_ID = os.environ.get("API_ID")
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL")
