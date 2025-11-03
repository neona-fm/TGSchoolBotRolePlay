from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from bot.config import BOT_TOKEN

# Новый способ задания parse_mode
bot = Bot(BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()
