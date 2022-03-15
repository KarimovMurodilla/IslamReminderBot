from aiogram import Bot, Dispatcher, types
from aiogram.utils.exceptions import MessageNotModified

from loader import bot, db
from app import buttons


async def callback_get_group_settings(c: types.CallbackQuery):
	user_id = c.from_user.id
	group_id = c.data[9:]

	await c.answer()
	await c.message.edit_text("Guruxingiz sozlamalari", 
        reply_markup = buttons.show_group_settings(group_id, db.get_data_from_group_id(group_id)[5]))


async def callback_change_rstatus(c: types.CallbackQuery):
	user_id = c.from_user.id
	group_id = c.data[15:]
	if db.get_data_from_group_id(group_id)[5] == '🟢':
		db.update_rStatus(group_id, '🔴')
		await c.answer("O'chdi")
	else:
		db.update_rStatus(group_id, '🟢')
		await c.answer("Yondi")

	await c.message.edit_text("Guruxingiz sozlamalari", 
        reply_markup = buttons.show_group_settings(group_id, db.get_data_from_group_id(group_id)[5]))


def register_callback_handlers(dp: Dispatcher):
	dp.register_callback_query_handler(callback_get_group_settings, lambda c: c.data.startswith('group_id'), state = '*')
	dp.register_callback_query_handler(callback_change_rstatus, lambda c: c.data.startswith('change_rStatus'), state = '*')