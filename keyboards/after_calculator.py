from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

after_calculator_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💬 Обсудить мой бизнес")],
        [KeyboardButton(text="🏠 Главное меню")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    is_persistent=False,
)