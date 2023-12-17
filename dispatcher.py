from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pytz import timezone
from config import TOKEN

scheduler = AsyncIOScheduler()

dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
moscow_tz = timezone('Europe/Moscow')
