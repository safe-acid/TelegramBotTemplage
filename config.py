import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

# Получаем токен бота
BOT_TOKEN = os.getenv("BOT_TOKEN")
