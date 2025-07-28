from aiogram import Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.menu import get_main_menu

def get_type_info_keyboard():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("👤 Индивидуальная", "💑 Love Story", "📷 Репортажная съёмка")
    kb.add("🔙 Назад")
    return kb

async def session_info_menu(message: types.Message):
    await message.answer("ℹ️ Выберите тип фотосессии, чтобы узнать подробнее:", reply_markup=get_type_info_keyboard())

async def show_info(message: types.Message):
    if message.text == "👤 Индивидуальная":
        await message.answer_photo(
            photo="https://clck.ru/3NJ9zC",
            caption=(
            "Индивидуальная фотосессия — запечатлейте уникальные моменты своей жизни!\n"
            "Индивидуальная фотосессия — это невероятная возможность создать неповторимые снимки, которые отражают вашу личность, стиль и эмоции.\n"
            "Это не просто фотографии, а целое искусство, созданное специально для вас!\n"
            "Стоимость - 1500 ₽/час\n"
            "В стоимость съёмки входит:\n"
            "- помощь в выборе идеи и образа к ней\n"
            "- подбор локации или фотостудии(оплачивается отдельно)\n"
            "- исходники и 15 фотографий в обработке и ретуши на ваш выбор\n"
            "Срок выдачи фотографий 4 дня\n"
            ),
            parse_mode="HTML"
        )

    elif message.text == "💑 Love Story":
        await message.answer_photo(
            photo="https://clck.ru/3NJAe9",
            caption=(
            "Съёмка Love story — это процесс создания серии фотографий, которые отражают историю любви между двумя людьми.\n"
            "Стоимость - 2000 ₽/час\n"
            "В стоимость съёмки входит:\n"
            "- помощь в выборе идеи и образа к ней\n"
            "- подбор локации или фотостудии (оплачивается отдельно)\n"
            "- исходники и 20 фотографий в обработке и ретуши на ваш выбор\n"
            "Срок выдачи фотографий 5 дней\n"
            ),
            parse_mode="HTML"
        )

    elif message.text == "📷 Репортажная съёмка":
        await message.answer_photo(
            photo="https://clck.ru/3NJAYr",
            caption=(
            "- репортажная съёмка разных событий, мероприятий и торжеств\n"
            "- фестивали, концерты, игры\n"
            "- дни рождения\n"
            "- корпоративные фотосъёмки\n"
            "Стоимость - 2000 ₽/час\n"
            "Вы получаете все фотографии в базовой цветокорекции\n"
            ),
            parse_mode="HTML"
        )

    elif message.text == "🔙 Назад":
        await message.answer("↩️ Главное меню", reply_markup=get_main_menu())

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(session_info_menu, lambda m: m.text == "ℹ️ Подробнее о типах фотосессии")
    dp.register_message_handler(show_info, lambda m: m.text in [
        "👤 Индивидуальная", "💑 Love Story", "📷 Репортажная съёмка", "🔙 Назад"
    ])
