from aiogram import types
from loader import db


def show_dashboard(user_id):
	dashboard = types.InlineKeyboardMarkup()
	for i in db.get_my_groups(user_id):
		groups = types.InlineKeyboardButton(text = i[1], callback_data = f"group_id {i[0]}")
		dashboard.add(groups)

	return dashboard


def show_group_settings(group_id, status):
	settings = types.InlineKeyboardMarkup()
	r_status = types.InlineKeyboardButton(text = f'Namoz vaqtini eslatish {status}', callback_data = f'change_rStatus {group_id}')
	settings.add(r_status)

	return settings