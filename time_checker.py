import os
import time
import random
import datetime

from aiogram import Bot
from aiogram.utils.exceptions import BotBlocked, TelegramAPIError
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from loader import bot, db
from app.data import NAMAZ_NAMES
from azan_times import NamazTimes, NAMAZ_TIMES

scheduler = AsyncIOScheduler()

async def send_remind():
    # server_time = datetime.datetime.today() + datetime.timedelta(hours=4)
    time_now = datetime.datetime.now().strftime('%H:%M')
    response = [(key, db.get_group_id_of_country(key)[0]) for key in NAMAZ_TIMES.keys() if time_now in NAMAZ_TIMES[key] and db.get_group_id_of_country(key)]
    
    for i in response:
        try:
            if NAMAZ_NAMES[d[i[0]].index(time_now)] == 'Quyosh':
                await bot.send_message(i[1], 
                    f"<b>Assalomu Aleykum\nVa Rahmatullohi va Barokotuh.</b>\n\n"
                    f"<i>Quyosh chiqishi vaqti bo'ldi</i>")

            else:
                await bot.send_audio(i[1], random.choice([a[0] for a in db.get_azan_audios()])),
                await bot.send_message(i[1], 
                    f"<b>Assalomu Aleykum\nVa Rahmatullohi va Barokotuh.</b>\n\n"
                    f"<i>{NAMAZ_NAMES[d[i[0]].index(time_now)]} namozi vaqti bo'ldilar</i>")
        
        except BotBlocked:
            await bot.send_message(875587704, f"{BotBlocked}")
            continue

        except TelegramAPIError:
            await bot.send_message(875587704, f"{TelegramAPIError}")
            continue

        except Exception as e:
            await bot.send_message(875587704, f"{e}")


async def update_namaz_times():
    namaz_times = NamazTimes()
    namaz_times.get_country_times()



def schedule_jobs():
    scheduler.add_job(send_remind, 'interval', minutes=1)

    scheduler.add_job(update_namaz_times, 'interval', hours=5)
