from aiogram import types
from bot.loader import dp

@dp.message()
async def log_all_messages(message: types.Message):
    user = message.from_user
    print(f"📨 [{user.id}] {user.full_name}: {message.text}")
