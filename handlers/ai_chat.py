from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from keyboards.navigation import back_to_menu
from keyboards.main_menu import main_menu
from services.yandex_ai import ask_ai
from memory.chat_memory import add_message, get_history

router = Router()


class AIChat(StatesGroup):
    waiting_question = State()


@router.message(F.text == "🤖 Задать вопрос")
async def ai_start(message: Message, state: FSMContext):
    await state.set_state(AIChat.waiting_question)

    await message.answer(
        "🤖 <b>AI-помощник NEXORA</b>\n\n"
        "Я могу помочь по следующим вопросам:\n\n"
        "• бухгалтерия\n"
        "• налоги\n"
        "• регистрация ИП и ООО\n"
        "• автоматизация бизнеса\n"
        "• маркетплейсы\n\n"
        "💬 Просто напишите свой вопрос.",
        parse_mode="HTML",
        reply_markup=back_to_menu,
    )


@router.message(AIChat.waiting_question)
async def ai_question(message: Message, state: FSMContext):
    if message.text == "🏠 Главное меню":
        await state.clear()

        await message.answer(
            "🏠 Вы вернулись в главное меню.",
            reply_markup=main_menu,
        )
        return

    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action="typing",
    )

    try:
        user_id = message.from_user.id

        # Добавляем сообщение пользователя
        add_message(
            user_id=user_id,
            role="user",
            content=message.text,
        )

        # Получаем историю диалога
        messages = get_history(user_id)

        # Отправляем историю в AI
        answer = await ask_ai(messages)

        # Сохраняем ответ AI
        add_message(
            user_id=user_id,
            role="assistant",
            content=answer,
        )

        await message.answer(
            f"🤖 <b>NEXORA AI</b>\n\n{answer}",
            parse_mode="HTML",
            reply_markup=back_to_menu,
        )

    except Exception as e:
        print(f"AI ERROR: {e}")

        await message.answer(
            "⚠️ Не удалось получить ответ.\n\nПопробуйте ещё раз через минуту.",
            reply_markup=back_to_menu,
        )