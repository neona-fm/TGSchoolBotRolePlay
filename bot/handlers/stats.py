from aiogram import types
from bot.loader import dp

@dp.message(lambda m: m.text and "стат" in m.text.lower())
async def stats(message: types.Message):
    await message.answer("📊 Статистика пока отключена. Будет позже.")
