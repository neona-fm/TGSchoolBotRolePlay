# 📁 bot/handlers/menu.py

from aiogram import types
from bot.loader import dp, bot
from bot.utils.questions import generate_task
from bot.utils.user_data import USER_LEVELS, PENDING_TASKS
from bot.keyboards.default import get_level_keyboard, get_main_keyboard
from pathlib import Path
import json

# 📘 Путь к FAQ
FAQ_PATH = Path("bot/data/faq.json")

# 📚 Новая задача
@dp.message(lambda m: m.text == "📚 Новая задача")
async def menu_task(message: types.Message):
    user_id = message.from_user.id
    level = USER_LEVELS.get(user_id, 1)

    question, answer = generate_task(level)
    PENDING_TASKS[user_id] = answer.strip()

    await message.answer(
        f"Реши (уровень {level} класс):\n\n<b>{question}</b>",
        parse_mode="HTML"
    )

# ❓ FAQ — Вопрос по обучению
@dp.message(lambda m: m.text == "❓ Вопрос по обучению")
async def menu_faq(message: types.Message):
    if FAQ_PATH.exists():
        with open(FAQ_PATH, encoding="utf-8") as f:
            faq_data = json.load(f)
    else:
        faq_data = {}

    if not faq_data:
        await message.answer("❌ FAQ пока пустой.")
        return

    text = "<b>Часто задаваемые вопросы:</b>\n\n"
    for q, a in faq_data.items():
        text += f"❓ <b>{q}</b>\n🟢 {a}\n\n"

    await message.answer(text.strip(), parse_mode="HTML")

# 📈 Статистика
@dp.message(lambda m: m.text == "📈 Статистика")
async def menu_stats(message: types.Message):
    await message.answer("📊 Статистика будет позже. Сейчас пока заглушка.")

# 🔁 Ещё одну задачу (по кнопке или тексту)
@dp.message(lambda m: m.text.lower() in {
    "да", "давай", "еще", "ещё", "хочу ещё", "хочу еще",
    "давай ещё", "давай еще", "ещё одну", "еще одну"
})
async def send_another_task(message: types.Message):
    user_id = message.from_user.id
    level = USER_LEVELS.get(user_id, 1)

    question, answer = generate_task(level)
    PENDING_TASKS[user_id] = answer.strip()

    await message.answer(
        f"Окей, вот новая задача:\n\n<b>{question}</b>",
        parse_mode="HTML"
    )

# 🎓 Выбор класса
@dp.message(lambda m: "выбрать класс" in m.text.lower())
async def ask_level(message: types.Message):
    await message.answer("🎓 Выбери свой класс:", reply_markup=get_level_keyboard())

# 📚 Установка уровня
@dp.message(lambda m: m.text.lower() in {"1 класс", "2 класс", "3 класс"})
async def set_level(message: types.Message):
    level_text = message.text.strip().split()[0]
    level_map = {"1": 1, "2": 2, "3": 3}
    level = level_map.get(level_text)

    if not level:
        await message.answer("🤷‍♂️ Не удалось распознать класс. Попробуй ещё раз.")
        return

    USER_LEVELS[message.from_user.id] = level
    await message.answer(
        f"📚 Уровень установлен: {level} класс\n\n🔁 Теперь можешь выбрать новую задачу:",
        reply_markup=get_main_keyboard()
    )

# 🔄 Универсальная функция — отправка новой задачи
async def send_new_task(user: types.User):
    """Используется при callback, чтобы бот писал пользователю, а не самому себе"""
    user_id = user.id
    level = USER_LEVELS.get(user_id, 1)

    question, answer = generate_task(level)
    PENDING_TASKS[user_id] = answer.strip()

    await bot.send_message(
        user_id,
        f"Реши (уровень {level} класс):\n\n<b>{question}</b>",
        parse_mode="HTML"
    )
