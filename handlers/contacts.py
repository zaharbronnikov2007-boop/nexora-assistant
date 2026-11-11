from aiogram import Router, F
from aiogram.types import Message

from keyboards.contacts import contacts_keyboard

router = Router()


@router.message(F.text == "📞 Контакты")
async def contacts(message: Message):
    await message.answer(
        "📞 <b>Контакты NEXORA</b>\n\n"

        "Мы всегда готовы помочь с:\n\n"

        "• бухгалтерией\n"
        "• налогами\n"
        "• регистрацией бизнеса\n"
        "• автоматизацией бизнеса\n\n"

        "🕘 <b>Время работы</b>\n"
        "Пн–Пт\n"
        "09:00–18:00\n\n"

        "👇 Выберите удобный способ связи.",

        parse_mode="HTML",
        reply_markup=contacts_keyboard
    )