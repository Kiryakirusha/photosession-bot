from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.menu import get_city_choice_keyboard, get_photosession_type_keyboard, get_main_menu
from config import PHOTOGRAPHER_ID

class Booking(StatesGroup):
    city = State()
    session_type = State()

# Команда: 📅 Записаться на фотосессию
async def start_booking(message: types.Message):
    await message.answer("📍 Из какого вы города?", reply_markup=get_city_choice_keyboard())
    await Booking.city.set()

# Обработка города
async def process_city(message: types.Message, state: FSMContext):
    if message.text == "🏙 Севастополь":
        await state.update_data(city="Севастополь")
    elif message.text == "🌐 Указать другой":
        await message.answer("✏️ Пожалуйста, напишите ваш город.")
        return
    elif message.text == "🔙 Назад":
        await state.finish()
        await message.answer("↩️ Возврат в главное меню", reply_markup=get_main_menu())
        return
    else:
        await state.update_data(city=message.text)

    await message.answer("📸 Выберите тип фотосессии:", reply_markup=get_photosession_type_keyboard())
    await Booking.session_type.set()

# Обработка типа съёмки
async def process_type(message: types.Message, state: FSMContext):
    if message.text == "🔙 Назад":
        await Booking.city.set()
        await message.answer("📍 Из какого вы города?", reply_markup=get_city_choice_keyboard())
        return

    valid_types = ["👤 Индивидуальная", "❤️ Love Story", "📷 Репортажная съёмка"]
    if message.text not in valid_types:
        await message.answer("❌ Пожалуйста, выберите тип фотосессии из списка.")
        return

    await state.update_data(session_type=message.text)
    data = await state.get_data()
    await state.finish()

    # Сообщение пользователю
    await message.answer("✅ Спасибо! Мы передали вашу заявку фотографу. Он скоро с вами свяжется.", reply_markup=get_main_menu())

    # Уведомление фотографу
    msg_to_photographer = (
        "🆕 <b>Новая заявка на фотосессию</b>\n\n"
        f"📍 Город: <b>{data['city']}</b>\n"
        f"📷 Тип: <b>{data['session_type']}</b>\n"
        f"👤 Имя: {message.from_user.full_name}\n"
        f"🔗 Username: @{message.from_user.username or 'нет'}\n"
        f"🆔 ID: <code>{message.from_user.id}</code>"
    )

    await message.bot.send_message(PHOTOGRAPHER_ID, msg_to_photographer, parse_mode="HTML")

# Регистрация
def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_booking, lambda m: m.text == "📅 Записаться на фотосессию")
    dp.register_message_handler(process_city, state=Booking.city)
    dp.register_message_handler(process_type, state=Booking.session_type)