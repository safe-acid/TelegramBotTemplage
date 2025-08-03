from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from config import BOT_TOKEN

# Инициализация бота с настройками по умолчанию (например, HTML разметка)
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)

# Создаём диспетчер — ядро маршрутизации
dp = Dispatcher()

# Пример простого обработчика всех входящих сообщений
@dp.message()
async def echo(message: types.Message):
    # Отвечаем на любое сообщение
    await message.answer("✅ Бот работает!")
