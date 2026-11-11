from aiogram import Router, F
from aiogram.types import Message

from keyboards.services import services_keyboard
from keyboards.main_menu import main_menu

router = Router()


@router.message(F.text == "💼 Наши услуги")
async def services(message: Message):
    await message.answer(
        "💼 <b>Услуги NEXORA</b>\n\n"
        "Выберите интересующее направление 👇",
        parse_mode="HTML",
        reply_markup=services_keyboard
    )


@router.message(F.text == "📚 Бухгалтерия")
async def accounting(message: Message):
    await message.answer(
        "📚 <b>Бухгалтерское сопровождение</b>\n\n"
        "✔ Полное ведение бухгалтерского учета\n"
        "✔ Расчет налогов\n"
        "✔ Расчет заработной платы\n"
        "✔ Работа с первичной документацией\n"
        "✔ Подготовка и сдача отчетности\n"
        "✔ Консультации бухгалтера\n\n"
        "💰 Хотите узнать стоимость?\n"
        "Нажмите «Рассчитать стоимость» в главном меню.",
        parse_mode="HTML"
    )


@router.message(F.text == "🧾 Отчетность")
async def reports(message: Message):
    await message.answer(
        "🧾 <b>Налоговая и бухгалтерская отчетность</b>\n\n"
        "✔ Подготовка деклараций\n"
        "✔ Сдача отчетности в ФНС\n"
        "✔ Отчетность в СФР\n"
        "✔ Исправление ошибок прошлых периодов\n"
        "✔ Контроль сроков сдачи",
        parse_mode="HTML"
    )


@router.message(F.text == "🏢 Регистрация бизнеса")
async def registration(message: Message):
    await message.answer(
        "🏢 <b>Регистрация бизнеса</b>\n\n"
        "✔ Регистрация ИП\n"
        "✔ Регистрация ООО\n"
        "✔ Выбор системы налогообложения\n"
        "✔ Подготовка документов\n"
        "✔ Консультация перед открытием бизнеса",
        parse_mode="HTML"
    )


@router.message(F.text == "🤖 Автоматизация")
async def automation(message: Message):
    await message.answer(
        "🤖 <b>Автоматизация бизнеса</b>\n\n"
        "✔ Внедрение CRM\n"
        "✔ Автоматизация процессов\n"
        "✔ Telegram-боты\n"
        "✔ Интеграции сервисов\n"
        "✔ Разработка внутренних систем",
        parse_mode="HTML"
    )


@router.message(F.text == "📈 Консультации")
async def consulting(message: Message):
    await message.answer(
        "📈 <b>Консультации</b>\n\n"
        "Мы поможем разобраться с:\n\n"
        "• налогами\n"
        "• бухгалтерией\n"
        "• регистрацией бизнеса\n"
        "• выбором системы налогообложения\n"
        "• оптимизацией бизнес-процессов\n\n"
        "🤝 Если вопрос сложный — подберем индивидуальное решение.",
        parse_mode="HTML"
    )


@router.message(F.text == "🏠 Главное меню")
async def back_to_main(message: Message):
    await message.answer(
        "🏠 Главное меню",
        reply_markup=main_menu
    )