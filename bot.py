from aiogram import Bot, Dispatcher
from aiogram import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import BOT_TOKEN
from handlers import start, misc, registration, about_photographer, session_info

# Создаём бота и хранилище состояний
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()  # FSM-хранилище в памяти
dp = Dispatcher(bot, storage=storage)

# Регистрируем все обработчики до запуска бота
start.register_handlers(dp)
registration.register_handlers(dp)
about_photographer.register_handlers(dp)
session_info.register_handlers(dp)
misc.register_handlers(dp)


if __name__ == '__main__':
    print("✅ Бот запущен")
    executor.start_polling(dp, skip_updates=True)