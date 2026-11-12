from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💬 Обсудить мой бизнес"),
        ],
        [
            KeyboardButton(text="💰 Рассчитать стоимость"),
            KeyboardButton(text="🤖 Задать вопрос"),
        ],
        [
            KeyboardButton(text="💼 Наши услуги"),
            KeyboardButton(text="📞 Контакты"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите действие..."
)

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

calculator_result_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💬 Обсудить мой бизнес")],
        [KeyboardButton(text="🤖 Задать вопрос")],
        [KeyboardButton(text="🏠 Главное меню")],
    ],
    resize_keyboard=True,
)