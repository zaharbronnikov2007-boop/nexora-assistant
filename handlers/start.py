from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.main_menu import main_menu

router = Router()


@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "👋 <b>Добро пожаловать в NEXORA!</b>\n\n"
        "Я цифровой помощник компании.\n\n"
        "Помогу подобрать бухгалтерское сопровождение, "
        "рассчитать стоимость услуг и ответить на популярные вопросы.\n\n"
        "👇 Выберите, с чего начнём.",
        reply_markup=main_menu,
        parse_mode="HTML"
    )