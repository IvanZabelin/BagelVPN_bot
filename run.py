import asyncio
import logging

from aiogram import Bot, Dispatcher

from config.settings import token
from app.handlers import router
from app.instruction import router as instruction_router
from app.check_subscriptions import check_subscriptions


bot = Bot(token=token)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    dp.include_router(instruction_router)
    asyncio.create_task(check_subscriptions())
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Bot stopped by user")
