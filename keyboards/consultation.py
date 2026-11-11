from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

business_type_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🧑 ИП"),
            KeyboardButton(text="🏢 ООО"),
        ],
        [
            KeyboardButton(text="👤 Самозанятый"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите статус..."
)

tax_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="УСН"),
            KeyboardButton(text="ОСНО"),
        ],
        [
            KeyboardButton(text="Патент"),
            KeyboardButton(text="Пока не знаю"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите систему..."
)

activity_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛍 Торговля")],
        [KeyboardButton(text="💻 Услуги")],
        [KeyboardButton(text="🏗 Строительство / Производство")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите вид деятельности..."
)

employees_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Нет"),
            KeyboardButton(text="1–5"),
        ],
        [
            KeyboardButton(text="6–20"),
            KeyboardButton(text="20+"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Количество сотрудников..."
)

patent_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Да"),
            KeyboardButton(text="Нет"),
        ]
    ],
    resize_keyboard=True,
)

vat_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Да"),
            KeyboardButton(text="Нет"),
        ]
    ],
    resize_keyboard=True,
)

service_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📚 Бухгалтерское сопровождение")],
        [KeyboardButton(text="⚙️ Автоматизация бизнеса")],
        [KeyboardButton(text="💰 Налоговая консультация")],
        [KeyboardButton(text="🏢 Регистрация бизнеса")],
        [KeyboardButton(text="📌 Другое")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите услугу..."
)

phone_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="📱 Отправить номер телефона",
                request_contact=True,
            )
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)