from aiogram import types
from bot.loader import dp
from bot.utils.questions import generate_task
from bot.utils.user_data import PENDING_TASKS, USER_LEVELS

@dp.message(lambda m: m.text and "задача" in m.text.lower())
async def send_task(message: types.Message):
    user_id = message.from_user.id
    level = USER_LEVELS.get(user_id, 1)  # По умолчанию 1 класс

    question, answer = generate_task(level)
    PENDING_TASKS[user_id] = answer.strip()

    await message.answer(f"Реши (уровень {level} класс):\n\n<b>{question}</b>", parse_mode="HTML")
