from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext

from states.calculator import CalculatorState
from services.calculator import calculate_price

router = Router()

# ---------- КЛАВИАТУРЫ ----------

business_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🧑 ИП"),
            KeyboardButton(text="🏢 ООО"),
        ]
    ],
    resize_keyboard=True,
)

tax_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="УСН"),
            KeyboardButton(text="УСН 15%"),
        ],
        [
            KeyboardButton(text="ОСНО"),
        ]
    ],
    resize_keyboard=True,
)

activity_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💻 Услуги")],
        [KeyboardButton(text="🛒 Торговля")],
        [KeyboardButton(text="🏗 Строительство / Производство")],
    ],
    resize_keyboard=True,
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
)

yes_no_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Да"),
            KeyboardButton(text="Нет"),
        ]
    ],
    resize_keyboard=True,
)

# ---------- СТАРТ ----------

@router.message(F.text == "💰 Рассчитать стоимость")
async def calculator_start(message: Message, state: FSMContext):
    await state.clear()

    await state.set_state(CalculatorState.business_type)

    await message.answer(
        "🧮 <b>Калькулятор NEXORA</b>\n\n"
        "Ответьте на несколько вопросов и получите примерную стоимость обслуживания.",
        parse_mode="HTML",
    )

    await message.answer(
        "🏢 Выберите форму бизнеса:",
        reply_markup=business_keyboard,
    )


@router.message(CalculatorState.business_type)
async def business_type(message: Message, state: FSMContext):
    await state.update_data(business_type=message.text)

    await state.set_state(CalculatorState.tax_system)

    await message.answer(
        "💰 Выберите систему налогообложения:",
        reply_markup=tax_keyboard,
    )


@router.message(CalculatorState.tax_system)
async def tax_system(message: Message, state: FSMContext):
    await state.update_data(tax_system=message.text)

    await state.set_state(CalculatorState.activity)

    await message.answer(
        "🏗 Чем занимается компания?",
        reply_markup=activity_keyboard,
    )


@router.message(CalculatorState.activity)
async def activity(message: Message, state: FSMContext):
    await state.update_data(activity=message.text.replace("💻 ", "").replace("🛒 ", "").replace("🏗 ", ""))

    await state.set_state(CalculatorState.employees)

    await message.answer(
        "👥 Сколько сотрудников работает?",
        reply_markup=employees_keyboard,
    )


@router.message(CalculatorState.employees)
async def employees(message: Message, state: FSMContext):
    await state.update_data(employees=message.text)

    await state.set_state(CalculatorState.operations)

    await message.answer(
        "📄 Сколько документов (операций) в месяц?\n\nНапишите только число."
    )
@router.message(CalculatorState.operations)
async def operations(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("❌ Введите только число.")
        return

    await state.update_data(operations=int(message.text))

    await state.set_state(CalculatorState.patent)

    await message.answer(
        "📑 Используется патент?",
        reply_markup=yes_no_keyboard,
    )


@router.message(CalculatorState.patent)
async def patent(message: Message, state: FSMContext):
    await state.update_data(
        patent=message.text == "Да"
    )

    await state.set_state(CalculatorState.vat)

    await message.answer(
        "🧾 Работаете с НДС на УСН?",
        reply_markup=yes_no_keyboard,
    )


@router.message(CalculatorState.vat)
async def vat(message: Message, state: FSMContext):
    await state.update_data(
        vat=message.text == "Да"
    )

    data = await state.get_data()

    # Тип компании
    if data["business_type"] == "🧑 ИП":
        if data["employees"] == "Нет":
            company_type = "ИП без сотрудников"
        else:
            company_type = "ИП с сотрудниками"
    else:
        company_type = "ООО"

    # Сотрудники
    employees_map = {
        "Нет": 0,
        "1–5": 3,
        "6–20": 10,
        "20+": 25,
    }

    price = calculate_price(
        company_type=company_type,
        tax=data["tax_system"],
        activity=data["activity"],
        employees=employees_map[data["employees"]],
        operations=data["operations"],
        patent=data["patent"],
        vat_usn=data["vat"],
    )

    await message.answer(
        f"""💰 <b>Предварительная стоимость</b>

≈ <b>{price:,} ₽ / месяц</b>

Это ориентировочная стоимость.

Для получения точного коммерческого предложения нажмите:

💬 <b>Обсудить мой бизнес</b>
""".replace(",", " "),
        parse_mode="HTML",
    )

    await state.clear()
