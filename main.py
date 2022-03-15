import asyncio
import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.types import BotCommand
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from loader import bot
from app.config import BOT_TOKEN
from time_checker import schedule_jobs, scheduler
from app.handlers.commands import register_cmd_handlers
from app.handlers.settings import register_settings_handlers
from app.handlers.callbacks import register_callback_handlers




async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Start Bot"),
        BotCommand(command="/dashboard", description="List of available groups")
    ]
    await bot.set_my_commands(commands)


async def main(dp):
	logging.basicConfig(level=logging.INFO)
	
	register_cmd_handlers(dp)
	register_settings_handlers(dp)
	register_callback_handlers(dp)

	schedule_jobs()

	await set_commands(bot)

	# await dp.start_polling()



if __name__ == '__main__':
	storage = MemoryStorage()
	dp = Dispatcher(bot, storage = storage)
	scheduler.start()
	executor.start_polling(dp, on_startup = main)