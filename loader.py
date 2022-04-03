from aiogram import Bot
from app.config import BOT_TOKEN
from app.connection import Database

# aiogram
bot = Bot(token=BOT_TOKEN, parse_mode = 'html')
db = Database(r"/root/IslamReminderBot/databases/main_db.db")

# requests
urls = ["https://islom.uz/region/", 'https://islom.uz/vaqtlar/2/3']
agent = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}