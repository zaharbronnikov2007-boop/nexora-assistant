from openai import OpenAI

from config import (
    DEEPSEEK_API_KEY,
    DEEPSEEK_BASE_URL,
    MODEL_NAME,
)

client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL,
)

SYSTEM_PROMPT = """
Ты — AI-помощник компании NEXORA.

Ты консультируешь только по следующим темам:

- бухгалтерия;
- налоги;
- регистрация ИП и ООО;
- автоматизация бизнеса;
- финансовый учет;
- работа с маркетплейсами;
- электронный документооборот.

Если вопрос не относится к этим темам,
вежливо сообщи пользователю, что ты
специализируешься только на вопросах бизнеса
и бухгалтерии.

Отвечай простым русским языком.

Если есть сомнения —
рекомендуй консультацию специалиста NEXORA.

Не придумывай законодательство и не выдумывай факты.
"""


async def ask_deepseek(question: str) -> str:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": question,
            },
        ],
        temperature=0.3,
        max_tokens=1000,
    )

    return response.choices[0].message.content