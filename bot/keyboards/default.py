from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_keyboard():
    keyboard = [
        [KeyboardButton(text="📚 Новая задача"), KeyboardButton(text="🎓 Выбрать класс")],
        [KeyboardButton(text="❓ Вопрос по обучению")],
        [KeyboardButton(text="📈 Статистика")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def get_level_keyboard():
    keyboard = [
        [KeyboardButton(text="1 класс"), KeyboardButton(text="2 класс"), KeyboardButton(text="3 класс")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
    
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

new_task_markup = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📚 Новая задача", callback_data="new_task")]
])
