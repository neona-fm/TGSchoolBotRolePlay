from aiogram import types
from aiogram.filters import CommandStart
from bot.loader import dp, bot
from bot.keyboards.default import get_main_keyboard
from bot.config import OWNER_CHAT_ID

# 📥 Обработка команды /start
@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    user = message.from_user

    # Уведомление владельцу
    text = (
        f"🚀 Бот запущен новым пользователем!\n\n"
        f"👤 <b>{user.full_name}</b>\n"
        f"🆔 <code>{user.id}</code>\n"
        f"🗣 Username: @{user.username if user.username else '—'}"
    )
    await bot.send_message(chat_id=OWNER_CHAT_ID, text=text, parse_mode="HTML")

    # Ответ пользователю
    await message.answer(
        "Привет! Я учебный бот. Готов помочь тебе с задачами, ответами и прочим.\n\nВыбери, что хочешь сделать:",
        reply_markup=get_main_keyboard()
    )

