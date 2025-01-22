from aiogram import Bot,Dispatcher

from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.session.aiohttp import AiohttpSession
TOKEN = "8019603194:AAEiA6Bssq_qgDGHnAfSHgcI9uGHSSyeYc8"

bot = Bot(token = TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())