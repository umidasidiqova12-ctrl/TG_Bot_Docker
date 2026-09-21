import asyncio
import logging
import sys
from os import getenv


from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "8696"

dp = Dispatcher()

# from aiogram import Router, F
# from aiogram.types import Message
# from aiogram.filters import Command

def start_manu():
    rkg = ReplyKeyboardBuilder()
    rkg.add(
        KeyboardButton(text="🏢 О компании"),
        KeyboardButton(text="💼 Вакансии"),
        KeyboardButton(text="📱 Меню"),
        KeyboardButton(text="📰 Новости"),
        KeyboardButton(text="📞 Контакты/Адрес"),
        KeyboardButton(text="💬 Обратная связь"),
        KeyboardButton(text="🇷🇺/🇺🇿 Язык")
    )

    rkg.adjust(1, 1, 2, 3, repeat=True)
    markup = rkg.as_markup(resize_keyboard=True)
    return markup

# @dp.message()
# async def any_message(message: Message):
#     print(message.photo[0].file_id)


# @dp.message()
# async def any_message(message: Message):
#     print(message.location.latitude)
# 41.302196, 69.248867


@dp.message(F.text == '/start')
async def start_handler(message: Message):
    markup = start_manu()
    await message.answer_photo("AgACAgIAAxkBAAOkacT2JRATV3ABqmVljxKoPEYX2jkAAg8VaxvbcyhKmXFeI8o8AAERAQADAgADcwADOgQ", reply_markup=markup)


@dp.message(F.text =="🏢 О компании")
async def about_us_handler(message: Message):
    text = """
    EVOS ® tez xizmat ko'rsatish restoranlari tarmog'i bir joyda turmaydi, siz uchun va siz bilan doimo o'sib boradi va rivojlanadi! Biz geografiyamizni kengaytiramiz va deyarli har oyda yangi filiallarni ochamiz.
Endi bizning tarmog'imizning O'zbekiston bo'ylab 50 dan ortiq filiali mavjud. Biz doimo jamoamizning bir qismi bo'lishni xohlaydigan va EVOS ® da o'z faoliyatini boshlashga tayyor bo'lgan dinamik va faol odamlarni qidiramiz.
EVOS ® –  bu ishonchli brenddir. EVOS ® da ishlash – barqaror daromad va martaba istiqbollari kafolati.
EVOS ® da o'z karyerangizni boshlang!
    """
    await message.answer_photo("AgACAgIAAxkBAAIBOWneJYUwc_tA_rNDFXjS6t-DY0qKAAIaF2sbV9_xSlwSwrvZEhH7AQADAgADcwADOwQ", caption=text)

# AgACAgIAAxkBAAIBOWneJYUwc_tA_rNDFXjS6t-DY0qKAAIaF2sbV9_xSlwSwrvZEhH7AQADAgADcwADOwQ

@dp.message(F.text =="📞 Контакты/Адрес")
async def adresas_handler(message: Message):
    text = """

Manzil: Furqat ko'chasi 175, kirish 1,
2-qavat.
Mo'ljal: MAKRO THE TOWER

Kontakt: +998 71 203 12 12
    """
    lat =41.302196
    long = 69.248867
    # image_id =
    await message.answer_photo("AgACAgIAAxkBAAIBOWneJYUwc_tA_rNDFXjS6t-DY0qKAAIaF2sbV9_xSlwSwrvZEhH7AQADAgADcwADOwQ", caption=text)
    await message.answer_location(lat, long)



async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


