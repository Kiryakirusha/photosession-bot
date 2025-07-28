from aiogram import Dispatcher, types
from keyboards.menu import get_main_menu

async def cmd_start(message: types.Message):
    await message.answer("Привет! 📷\nВыберите, что вас интересует:", reply_markup=get_main_menu())

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start")
