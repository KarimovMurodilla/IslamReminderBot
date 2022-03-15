import os
import time
import random
import datetime

from aiogram import Bot
from aiogram.utils.exceptions import BotBlocked, TelegramAPIError
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from loader import bot, db
from azan_times import times

scheduler = AsyncIOScheduler()

async def send_remind():
    server_time = datetime.datetime.today() + datetime.timedelta(hours=4)
    time_now = server_time.strftime('%H:%M')
    times_data = times()
    if time_now in times_data:
        for i in db.get_enabled_rstatuses():
            try:
                if times_data[time_now] == 'Quyosh':
                    await bot.send_message(i[0], 
                        f"<b>Assalomu Aleykum\nVa Rahmatullohi va Barokotuh.</b>\n\n"
                        f"<i>Quyosh chiqishi vaqti bo'ldi</i>")

                else:
                    await bot.send_audio(i[0], random.choice([a[0] for a in db.get_azan_audios()])),
                    await bot.send_message(i[0], 
                        f"<b>Assalomu Aleykum\nVa Rahmatullohi va Barokotuh.</b>\n\n"
                        f"<i>{times_data[time_now]} namozi vaqti bo'ldilar</i>")
            
            except BotBlocked:
                await bot.send_message(875587704, f"{BotBlocked}")
                continue

            except TelegramAPIError:
                await bot.send_message(875587704, f"{TelegramAPIError}")
                continue



def schedule_jobs():
    scheduler.add_job(send_remind, 'interval', seconds=5)
