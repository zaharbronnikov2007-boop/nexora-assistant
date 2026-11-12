from services.telegram_notify import send_consultation
from services.logger import log_lead
from aiogram import Router, F
from aiogram.types import Message
from keyboards.main_menu import calculator_result_keyboard

from aiogram.fsm.context import FSMContext

from states.consultation import ConsultationState

from keyboards.consultation import (
    business_type_keyboard,
    tax_keyboard,
    employees_keyboard,
    service_keyboard,
    phone_keyboard,
)

router = Router()


@router.message(F.text == "💬 Обсудить мой бизнес")
async def consultation_start(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(ConsultationState.name)

    await message.answer(
        "👋 Отлично!\n\n"
        "Давайте познакомимся.\n\n"
        "Как мне к вам обращаться?"
    )


@router.message(ConsultationState.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)

    await state.set_state(ConsultationState.business_type)

    await message.answer(
        f"Приятно познакомиться, <b>{message.text}</b>! 👋\n\n"
        "🏢 Кто вы?",
        reply_markup=business_type_keyboard,
        parse_mode="HTML"
    )


@router.message(ConsultationState.business_type)
async def get_business_type(message: Message, state: FSMContext):
    await state.update_data(business_type=message.text)

    await state.set_state(ConsultationState.tax_system)

    await message.answer(
        "💰 Какая у вас система налогообложения?",
        reply_markup=tax_keyboard
    )


@router.message(ConsultationState.tax_system)
async def get_tax(message: Message, state: FSMContext):
    await state.update_data(tax_system=message.text)

    await state.set_state(ConsultationState.employees)

    await message.answer(
        "👥 Сколько сотрудников работает?",
        reply_markup=employees_keyboard
    )


@router.message(ConsultationState.employees)
async def get_employees(message: Message, state: FSMContext):
    await state.update_data(employees=message.text)

    await state.set_state(ConsultationState.service)

    await message.answer(
        "📚 Какая услуга вас интересует?",
        reply_markup=service_keyboard
    )


@router.message(ConsultationState.service)
async def get_service(message: Message, state: FSMContext):
    await state.update_data(service=message.text)

    await state.set_state(ConsultationState.description)

    await message.answer(
        "✍️ Коротко опишите вашу ситуацию."
    )


@router.message(ConsultationState.description)
async def get_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)

    await state.set_state(ConsultationState.phone)

    await message.answer(
        "📱 Отправьте номер телефона.",
        reply_markup=phone_keyboard
    )


@router.message(ConsultationState.phone)
async def get_phone(message: Message, state: FSMContext):
    phone = (
        message.contact.phone_number
        if message.contact
        else message.text
    )

    await state.update_data(phone=phone)

    data = await state.get_data()

    log_lead(data)

    await send_consultation(
        message.bot,
        data,
    )

    await message.answer(
    "✅ Спасибо!\n\n"
    "Ваша заявка отправлена специалисту NEXORA.\n\n"
    "Мы свяжемся с вами в ближайшее время.",
    reply_markup=calculator_result_keyboard,
)