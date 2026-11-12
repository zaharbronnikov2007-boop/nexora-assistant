import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from handlers.consultation import router as consultation_router
from handlers.start import router as start_router
from keyboards.main_menu import main_menu
from handlers.questionnaire import router as questionnaire_router
from handlers.ai_chat import router as ai_chat_router
from handlers.services import router as services_router
from handlers.contacts import router as contacts_router
from handlers.calculator import router as calculator_router
from handlers.admin import router as admin_router

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(start_router)
dp.include_router(consultation_router)
dp.include_router(questionnaire_router)
dp.include_router(ai_chat_router)
dp.include_router(services_router)
dp.include_router(contacts_router)
dp.include_router(calculator_router)
dp.include_router(admin_router)

async def main():
    me = await bot.get_me()
    print(me)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())