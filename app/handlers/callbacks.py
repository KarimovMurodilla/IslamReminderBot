from aiogram import Bot, Dispatcher, types
from aiogram.utils.exceptions import MessageNotModified

from loader import bot, db
from app import buttons


async def callback_get_group_settings(c: types.CallbackQuery):
	user_id = c.from_user.id
	group_id = c.data[9:]
	group_name = db.get_data_from_group_id(group_id)[2]

	await c.answer()
	await c.message.edit_text(f"<b>{group_name}</b> guruxining sozlamalari:", 
		reply_markup = buttons.show_group_settings(
			group_id = group_id, 
			status_remind = db.get_data_from_group_id(group_id)[5]))


async def callback_change_rstatus(c: types.CallbackQuery):
	user_id = c.from_user.id
	group_id = c.data[15:]
	group_name = db.get_data_from_group_id(group_id)[2]

	if db.get_data_from_group_id(group_id)[5] == '🟢':
		db.update_rStatus(group_id, '🔴')
		await c.answer("O'chdi")
	else:
		db.update_rStatus(group_id, '🟢')
		await c.answer("Yondi")

	await c.message.edit_text(f"<b>{group_name}</b> guruxining sozlamalari:", 
		reply_markup = buttons.show_group_settings(
			group_id = group_id, 
			status_remind = db.get_data_from_group_id(group_id)[5]))


async def callback_show_audios(c: types.CallbackQuery):
	await c.answer()
	group_id = c.data[12:]
	await c.message.edit_text("Azon ovozlarining ro'yhati:",
		reply_markup = buttons.show_audios(group_id))


async def callback_show_list_of_countries(c: types.CallbackQuery):
	await c.answer()
	group_id = c.data[15:]
	await c.message.edit_text("Mintaqalar ro'yhati:",
		reply_markup = buttons.show_countries(group_id))


async def callback_set_location(c: types.CallbackQuery):
	await c.answer()
	ids = c.data[13:].split(',')
	group_id = ids[1]
	country_name = ids[0]
	db.set_location(group_id, country_name)

	await c.message.edit_text("Mintaqalar ro'yhati:",
		reply_markup = buttons.show_countries(group_id))


# Back callbacks
async def callback_back_to_settings(c: types.CallbackQuery):
	user_id = c.from_user.id
	group_id = c.data[17:]
	group_name = db.get_data_from_group_id(group_id)[2]
	
	await c.answer()
	await c.message.edit_text(f"<b>{group_name}</b> guruxining sozlamalari:", 
		reply_markup = buttons.show_group_settings(
			group_id = group_id, 
			status_remind = db.get_data_from_group_id(group_id)[5]))


async def callback_back_to_dashboard(c: types.CallbackQuery):
	user_id = c.from_user.id

	await c.answer()
	await c.message.edit_text("Sizning guruxlaringiz ro'yhati", 
		reply_markup = buttons.show_dashboard(user_id))


def register_callback_handlers(dp: Dispatcher):
	dp.register_callback_query_handler(callback_get_group_settings, lambda c: c.data.startswith('group_id'), state = '*')
	dp.register_callback_query_handler(callback_change_rstatus, lambda c: c.data.startswith('change_rStatus'), state = '*')
	dp.register_callback_query_handler(callback_show_audios, lambda c: c.data.startswith('show_audios'), state = '*')
	dp.register_callback_query_handler(callback_show_list_of_countries, lambda c: c.data.startswith('show_countries'), state = '*')

	dp.register_callback_query_handler(callback_set_location, lambda c: c.data.startswith('set_location'), state = '*')
	
	dp.register_callback_query_handler(callback_back_to_settings, lambda c: c.data.startswith("back_to_settings"), state = '*')
	dp.register_callback_query_handler(callback_back_to_dashboard, lambda c: c.data == "back_to_dashboard", state = '*')
