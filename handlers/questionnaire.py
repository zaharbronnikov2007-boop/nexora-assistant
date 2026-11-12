from aiogram import Bot

from services.telegram_notify import send_consultation
from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from keyboards.main_menu import calculator_result_keyboard

from states.consultation import ConsultationState
from keyboards.consultation import (
    tax_keyboard,
    employees_keyboard,
    service_keyboard,
    phone_keyboard,
)

router = Router()


@router.message(ConsultationState.business_type)
async def business_type(message: Message, state: FSMContext):
    await state.update_data(business_type=message.text)

    await state.set_state(ConsultationState.tax_system)

    await message.answer(
        "📊 Какая система налогообложения?",
        reply_markup=tax_keyboard
    )


@router.message(ConsultationState.tax_system)
async def tax_system(message: Message, state: FSMContext):
    await state.update_data(tax_system=message.text)

    await state.set_state(ConsultationState.employees)

    await message.answer(
        "👥 Сколько сотрудников работает в компании?",
        reply_markup=employees_keyboard
    )


@router.message(ConsultationState.employees)
async def employees(message: Message, state: FSMContext):
    await state.update_data(employees=message.text)

    await state.set_state(ConsultationState.service)

    await message.answer(
        "💼 Какая услуга вас интересует?",
        reply_markup=service_keyboard
    )


@router.message(ConsultationState.service)
async def service(message: Message, state: FSMContext):
    await state.update_data(service=message.text)

    await state.set_state(ConsultationState.description)

    await message.answer(
        "✍️ Кратко опишите вашу задачу."
    )


@router.message(ConsultationState.description)
async def description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)

    await state.set_state(ConsultationState.phone)

    await message.answer(
        "📱 Теперь отправьте номер телефона.",
        reply_markup=phone_keyboard
    )


@router.message(ConsultationState.phone)
async def phone(message: Message, state: FSMContext):
    phone = (
        message.contact.phone_number
        if message.contact
        else message.text
    )

    await state.update_data(phone=phone)

    data = await state.get_data()

    await send_consultation(message.bot, data)

    await state.clear()

    await message.answer(
        "🎉 <b>Спасибо!</b>\n\n"
        "Ваша заявка успешно отправлена.\n\n"
        "Специалист NEXORA свяжется с вами в ближайшее рабочее время.",
        parse_mode="HTML",
        reply_markup=calculator_result_keyboard,
    )