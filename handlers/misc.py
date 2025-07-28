from aiogram import Dispatcher, types

# Команда /help
async def cmd_help(message: types.Message):
    print(f"Получена команда /help от {message.from_user.id}")
    await message.answer(
        "📸 *Бот для записи на фотосессию*\n\n"
        "Просто нажмите кнопку с нужным типом фотосессии.\n"
        "После этого мы передадим вашу заявку фотографу.\n\n"
        "Для возврата в меню нажмите /start",
        parse_mode="Markdown"
    )

# Обработка любых других текстов (например, случайных слов)
async def unknown_message(message: types.Message):
    await message.answer("❓ Я не понимаю это сообщение. Пожалуйста, выберите вариант из меню или нажмите /start")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_help, commands=["help"])
    dp.register_message_handler(unknown_message, content_types=types.ContentTypes.TEXT, state="*")
