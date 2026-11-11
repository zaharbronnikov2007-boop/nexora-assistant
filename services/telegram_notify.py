from aiogram import Bot

MANAGER_ID = 8974475820


async def send_consultation(bot: Bot, data: dict):
    text = (
        "📩 <b>Новая заявка NEXORA</b>\n\n"
        f"👤 <b>Имя:</b> {data['name']}\n"
        f"🏢 <b>Статус:</b> {data['business_type']}\n"
        f"📊 <b>Налоговая система:</b> {data['tax_system']}\n"
        f"👥 <b>Сотрудники:</b> {data['employees']}\n"
        f"💼 <b>Услуга:</b> {data['service']}\n\n"
        f"📝 <b>Описание:</b>\n{data['description']}\n\n"
        f"📱 <b>Телефон:</b> {data['phone']}"
    )

    await bot.send_message(
        chat_id=MANAGER_ID,
        text=text,
        parse_mode="HTML"
    )