from aiogram import Bot
from app.config import BOT_TOKEN
from app.connection import Database


bot = Bot(token=BOT_TOKEN, parse_mode = 'html')
db = Database(r"databases\main_db.db")