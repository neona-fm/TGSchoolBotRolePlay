from aiogram import types
from bot.loader import dp
import json
from pathlib import Path

FAQ_PATH = Path("bot/data/faq.json")

def load_faq():
    if FAQ_PATH.exists():
        with open(FAQ_PATH, encoding="utf-8") as f:
            return json.load(f)
    return {}

@dp.message(lambda m: m.text and "вопрос" in m.text.lower())
async def faq(message: types.Message):
    faq_data = load_faq()

    text = "<b>Часто задаваемые вопросы:</b>\n\n"
    for q, a in faq_data.items():
        text += f"❓ <b>{q}</b>\n🟢 {a}\n\n"

    await message.answer(text.strip(), parse_mode="HTML")
