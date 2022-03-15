from googletrans import Translator
from aiogram import Bot, Dispatcher, types
from loader import bot, db


# Register new chat in db
async def new_chat(message: types.Message):
    user_id = message.from_user.id
    group_id = message.chat.id
    group_title = message.chat.title

    db.reg_new_group(user_id, group_id, group_title)
    await bot.send_message(group_id, "Assalomu aleykum!")


async def leave_chat(message: types.Message):
    group_id = message.chat.id
    db.delete_group(group_id)


def register_settings_handlers(dp: Dispatcher):
    dp.register_message_handler(new_chat, content_types = 'new_chat_members', state = '*')
    dp.register_message_handler(leave_chat, content_types = 'left_chat_member', state = '*')
