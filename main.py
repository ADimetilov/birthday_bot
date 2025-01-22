import logging
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from aiogram import Bot,Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.session.aiohttp import AiohttpSession
import config
from handlers.drlist import return_list
from handlers.bot_command import router
async def main():
    try:
        bot = Bot(token = config.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
        dp = Dispatcher(storage=MemoryStorage())
        dp.include_router(router=router)
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot,allowed_updates=dp.resolve_used_update_types())
    except Exception as e:
        print("Произошла ошибка",str(e))
        await asyncio.run(main())

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

