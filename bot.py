import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

import database
from config import config
from routers import auth, back, common, menu, model, status


async def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")

    bot = Bot(config.bot_token.get_secret_value())
    dispatcher = Dispatcher(storage=MemoryStorage())
    dispatcher.include_routers(auth.router, back.router, common.router, menu.router, model.router, status.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot)


if __name__ == '__main__':
    database.init()
    asyncio.run(main())
