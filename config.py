import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
PHOTOGRAPHER_ID = int(os.getenv("PHOTOGRAPHER_ID"))
