from openai import OpenAI

from config import (
    YANDEX_API_KEY,
    YANDEX_FOLDER_ID,
)

client = OpenAI(
    api_key=YANDEX_API_KEY,
    project=YANDEX_FOLDER_ID,
    base_url="https://ai.api.cloud.yandex.net/v1",
)

SYSTEM_PROMPT = """
Ты — AI-помощник компании NEXORA.

Ты отвечаешь только на темы:

• бухгалтерия
• налоги
• регистрация бизнеса
• автоматизация бизнеса
• финансовый учет
• маркетплейсы

Если вопрос не относится к этим темам —
вежливо сообщи пользователю, что ты специализируешься
только на вопросах бизнеса и бухгалтерии.

Отвечай простым и понятным языком.

Если законодательство может измениться —
предупреди пользователя об этом.

Если не уверен —
порекомендуй обратиться к специалисту NEXORA.

Не придумывай факты.
"""


async def ask_ai(history: list) -> str:
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        }
    ]

    messages.extend(history)

    response = client.chat.completions.create(
        model=f"gpt://{YANDEX_FOLDER_ID}/yandexgpt/latest",
        messages=messages,
        temperature=0.3,
        max_tokens=1000,
    )

    return response.choices[0].message.content