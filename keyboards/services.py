from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

services_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📚 Бухгалтерия")],
        [KeyboardButton(text="🧾 Отчетность")],
        [KeyboardButton(text="🏢 Регистрация бизнеса")],
        [KeyboardButton(text="🤖 Автоматизация")],
        [KeyboardButton(text="📈 Консультации")],
        [KeyboardButton(text="🏠 Главное меню")],
    ],
    resize_keyboard=True,
)