import asyncio
import logging
from bot import bot, dp

# Настройка логов для вывода в терминал
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

# Главная асинхронная функция запуска бота
async def main():
    logging.info("🚀 Бот запускается...")
    while True:
        try:
            # Запускаем поллинг (прослушку входящих сообщений)
            await dp.start_polling(bot)
        except Exception as e:
            # В случае ошибки — логируем её и перезапускаем цикл через 5 секунд
            logging.error(f"❌ Ошибка: {e}. Перезапуск через 5 секунд...")
            await asyncio.sleep(5)

# Запускаем main() если этот файл запущен напрямую
if __name__ == "__main__":
    asyncio.run(main())
