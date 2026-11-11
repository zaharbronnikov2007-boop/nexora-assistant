from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

back_to_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏠 Главное меню"),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите действие..."
)