import os
from dotenv import load_dotenv

# Загружаем .env
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_CHAT_ID = os.getenv("OWNER_CHAT_ID")
FORWARD_ALL_QA = os.getenv("FORWARD_ALL_QA", "true").lower() == "true"
USE_WEBHOOK = os.getenv("USE_WEBHOOK", "false").lower() == "true"
WEBAPP_URL = os.getenv("WEBAPP_URL", "")
WEBHOOK_PATH = os.getenv("WEBHOOK_PATH", "/webhook")

if not BOT_TOKEN:
    raise RuntimeError("❌ BOT_TOKEN не указан в .env")
