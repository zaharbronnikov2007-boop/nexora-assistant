from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

contacts_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="💬 Telegram",
                url="https://t.me/nexorabuh_manager"
            )
        ],
        [
            InlineKeyboardButton(
                text="🌐 Сайт",
                url="https://www.nexora-buh.ru/"
            )
        ],
        [
            InlineKeyboardButton(
                text="📧 Email",
                url="https://nexora.ru"
            )
        ]
    ]
)