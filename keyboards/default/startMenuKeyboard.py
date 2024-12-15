from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Mahsulot🛒'),
            KeyboardButton(text="Yordam🛠")
        ],
    ],
    resize_keyboard=True
)

