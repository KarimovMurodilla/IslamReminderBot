from aiogram import Dispatcher, types
from loader import bot, db
from app import buttons


async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    db.checkUser(user_id)

    await message.answer(
        "Assalomu aleykum"
        )


async def on(message: types.Message):
    # await bot.set_chat_permissions(message.chat.id, permissions = types.ChatPermissions(can_send_messages = True))
    print(types.ChatPermissions(message.chat.id))


async def off(message: types.Message):
    await bot.set_chat_permissions(message.chat.id, permissions = types.ChatPermissions(can_send_messages = False))


async def cmd_dashboard(message: types.Message):
    user_id = message.from_user.id
    if message.chat.type == 'private':
        await message.answer("Assalomu aleykum\nSizning guruxlaringiz ro'yhati", 
            reply_markup = buttons.show_dashboard(user_id))


def register_cmd_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands = 'start', state="*")
    dp.register_message_handler(cmd_dashboard, commands = 'dashboard', state="*")

    dp.register_message_handler(on, commands = 'on', state="*")
    dp.register_message_handler(off, commands = 'off', state="*")


