from bot.loader import bot, dp
from bot.config import USE_WEBHOOK, WEBAPP_URL, WEBHOOK_PATH

# Импорт хендлеров (регистрируются при импорте)
from bot.handlers import start, tasks, faq, stats, menu, check_answer, logger


import asyncio

async def on_startup(bot):
    print("🚀 Бот запускается...")

async def main():
    if USE_WEBHOOK:
        webhook_url = WEBAPP_URL + WEBHOOK_PATH
        print(f"🔗 Вебхук: {webhook_url}")
        await bot.set_webhook(webhook_url)
        await dp.start_webhook(
            bot=bot,
            webhook_path=WEBHOOK_PATH,
            on_startup=on_startup
        )
    else:
        print("📡 Polling режим")
        await dp.start_polling(bot)

if __name__ == "__main__":
    print("📦 Запуск main() через asyncio.run")
    asyncio.run(main())
