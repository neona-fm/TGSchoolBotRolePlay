# 📥 Импорты
from aiogram import types
from bot.loader import dp
from bot.utils.user_data import PENDING_TASKS
from bot.keyboards.default import new_task_markup  # кнопка уже была

# 🔢 Проверка числового ответа
@dp.message(lambda m: m.text and m.text.strip().isdigit())
async def check_answer(message: types.Message):
    user_id = message.from_user.id
    user_input = message.text.strip()

    if user_id not in PENDING_TASKS:
        await message.answer("🤔 Я не задавал тебе задачу. Нажми '📚 Новая задача'.")
        return

    correct_answer = PENDING_TASKS.pop(user_id)

    if user_input == correct_answer:
        await message.answer("✅ Правильно! Хочешь ещё одну?", reply_markup=new_task_markup)
    else:
        await message.answer(
            f"❌ Неправильно. Правильный ответ был: <b>{correct_answer}</b>\n\n🔁 Хочешь ещё одну?",
            parse_mode="HTML",
            reply_markup=new_task_markup  # ✅ кнопка теперь есть и при ошибке
        )
# ✅ Обработка нажатия на кнопку "📚 Новая задача"
@dp.callback_query(lambda c: c.data == "new_task")
async def process_new_task_callback(callback_query: types.CallbackQuery):
    from bot.handlers.menu import send_new_task
    await callback_query.answer()
    await send_new_task(callback_query.from_user)

