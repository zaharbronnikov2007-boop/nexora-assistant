from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from keyboards.navigation import back_to_menu
from keyboards.main_menu import main_menu
from services.yandex_ai import ask_ai

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
        reply_markup=back_to_menu
    )


@router.message(AIChat.waiting_question)
async def ai_question(message: Message, state: FSMContext):
    if message.text == "🏠 Главное меню":
        await state.clear()

        await message.answer(
            "🏠 Вы вернулись в главное меню.",
            reply_markup=main_menu
        )
        return

    # Показываем статус "печатает..."
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action="typing"
    )

    try:
        history = await state.get_data()
        messages = history.get("history", [])

        # Добавляем сообщение пользователя
        messages.append(
            {
                "role": "user",
                "content": message.text
            }
        )

        # Храним только последние 20 сообщений
        messages = messages[-20:]

        answer = await ask_ai(messages)

        # Добавляем ответ ИИ в историю
        messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        await state.update_data(history=messages)

        await message.answer(
            f"🤖 <b>NEXORA AI</b>\n\n"
            f"{answer}",
            parse_mode="HTML",
            reply_markup=back_to_menu
        )

    except Exception as e:
        print(e)

        await message.answer(
            "⚠️ Не удалось получить ответ.\n\n"
            "Попробуйте ещё раз через минуту.",
            reply_markup=back_to_menu
        )