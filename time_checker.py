import os
import time
import datetime

from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from loader import bot, db
from azan_times import times

scheduler = AsyncIOScheduler()

async def send_remind():
    server_time = datetime.datetime.today() + datetime.timedelta(hours=4)
    if server_time.strftime('%H:%M') in times(): 
        mailing = [(
            await bot.send_audio(i[0], 'CQACAgIAAxkBAANiYi_1VWJZ6_UCByTH6FZ1CIrxA-AAAvkNAAInFIBLDUJocuQLRAgjBA'),

            await bot.send_message(i[0], 
                f"<b>Assalomu Aleykum\nVa Rahmatullohi va Barokotuh.</b>\n\n<i>Namoz vaqti bo'ldi birodar</i>")

            )
                for i in db.get_enabled_rstatuses()]

    print(server_time)


def schedule_jobs():
    scheduler.add_job(send_remind, 'interval', minutes=1)
