from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("📅 Записаться на фотосессию"))
    kb.add("📸 О фотографе", "ℹ️ Подробнее о типах фотосессии")
    return kb

def get_city_choice_keyboard():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("🏙 Севастополь"), KeyboardButton("🌐 Указать другой"))
    kb.add(KeyboardButton("🔙 Назад"))
    return kb

def get_photosession_type_keyboard():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("👤 Индивидуальная"))
    kb.add(KeyboardButton("❤️ Love Story"))
    kb.add(KeyboardButton("📷 Репортажная съёмка"))
    kb.add(KeyboardButton("🔙 Назад"))
    return kb