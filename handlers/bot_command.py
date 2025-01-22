from aiogram import Router,F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from datetime import datetime
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from handlers.drlist import return_list
from config import bot
import time
router = Router()
@router.message(Command("start"))
async def start_handler(msg:Message,bot:Bot):
    await msg.answer("Ку, я бот по др группы 11ИСиП232, чем вам помочь?")

@router.message(Command("start2"))
async def dr(msg:Message,bot:Bot):
    print(msg.chat.id)
    await msg.answer("Бот запущен, уведомления о днях рождениях активрованы!")
    asyncio.create_task(birthday(msg.chat.id,bot=bot))


async def birthday(group_id:int,bot:Bot):
    while True:
        time_now = datetime.now().strftime("%H:%M")
        if time_now == "00:00":
            date = datetime.now().strftime("%d.%m")
            for datedr in return_list():
                print(datedr)
                if datedr["date"] == date:
                    await bot.send_message(chat_id=group_id, text = f"Сегодня день рождения у <b>{datedr["name"] }</b>🎂")
        time.sleep(60.0)
        
