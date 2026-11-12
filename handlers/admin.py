from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from services.logger import stats

router = Router()

# ID администратора
ADMIN_ID = 8974475820


def is_admin(message: Message) -> bool:
    return message.from_user.id == ADMIN_ID


@router.message(Command("stats"))
async def stats_command(message: Message):
    if not is_admin(message):
        return

    data = stats()

    await message.answer(
        f"""📊 <b>Статистика NEXORA</b>

👥 Пользователей: <b>{data["users"]}</b>

🤖 AI запросов: <b>{data["ai"]}</b>

💰 Расчётов: <b>{data["calculator"]}</b>

📨 Заявок: <b>{data["leads"]}</b>
""",
        parse_mode="HTML",
    )


@router.message(Command("users"))
async def users(message: Message):
    if not is_admin(message):
        return

    await message.answer(
        "👥 Последние пользователи\n\n"
        "Функция появится на следующем этапе."
    )


@router.message(Command("leads"))
async def leads(message: Message):
    if not is_admin(message):
        return

    await message.answer(
        "📨 Последние заявки\n\n"
        "Функция появится на следующем этапе."
    )