from aiogram import Dispatcher, types
from keyboards.menu import get_main_menu

async def about_photographer(message: types.Message):
    photo_url = "https://sun9-10.userapi.com/s/v1/ig2/uB48tNm30XHBQ_vYzSZjZwLJzbELdU2r9QNYe2ueSZt96oNorE6ClBkFwldWvb5AjJvNHGikApLx8mJ1m6e7wbFQ.jpg?quality=95&as=32x48,48x71,72x107,108x161,160x238,240x357,360x536,480x715,540x804,640x953,720x1072,1080x1608,1280x1906,1440x2144,1719x2560&from=bu&cs=1280x0"  # ⚠️ Замени на реальную ссылку или используй send_photo с файлом
    caption = (
        "Привет! Меня зовут Палина,"
        "и я профессиональный фотограф с 5-ти летним опытом.\n"
        "Что я предлагаю:\n"
        "- Индивидуальные фотосессии\n"
        "- Love story\n"
        "- Корпоративные мероприятия\n"
        "Почему выбирают меня:\n"
        "- Индивидуальный подход к каждому клиенту\n"
        "- Высокое качество снимков и профессиональная обработка\n"
        "- Творческий взгляд и внимание к деталям\n"
        "- Доступные цены\n"
        "Где я работаю:\n"
        "Я нахожусь в Севастополе\n"
        "Буду рада помочь вам сохранить важные моменты вашей жизни в красивых фотографиях.\n"
        "Ознакомиться с моими работами можно в моем группе\n"
        "https://vk.com/fototokp?from=groups"
    )

    await message.answer_photo(photo=photo_url, caption=caption, parse_mode="HTML", reply_markup=get_main_menu())

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(about_photographer, lambda m: m.text == "📸 О фотографе")