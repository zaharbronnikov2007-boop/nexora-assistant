from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

YANDEX_API_KEY = os.getenv("YANDEX_API_KEY")
YANDEX_FOLDER_ID = os.getenv("YANDEX_FOLDER_ID")

YANDEX_BASE_URL = "https://ai.api.cloud.yandex.net/v1"
MODEL_NAME = f"gpt://{YANDEX_FOLDER_ID}/yandexgpt/latest"