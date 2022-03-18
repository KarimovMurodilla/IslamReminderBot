from aiogram import types
from loader import db


def show_dashboard(user_id):
	groups = db.get_my_groups(user_id)
	dashboard = types.InlineKeyboardMarkup(row_width = 2)
	for i in groups:
		group_btn = types.InlineKeyboardButton(text = i[1], callback_data = f"group_id {i[0]}")
		dashboard.add(group_btn)

	startgroup = types.InlineKeyboardMarkup(text = "➕", url = "https://t.me/IslamReminderBot?startgroup=new")
	dashboard.add(startgroup)

	return dashboard


def show_group_settings(group_id, status):
	settings = types.InlineKeyboardMarkup()
	r_status = types.InlineKeyboardButton(text = f'Namoz vaqtini eslatish {status}', callback_data = f'change_rStatus {group_id}')
	btn_back = types.InlineKeyboardMarkup(text = "⬅️ Orqaga", callback_data = "back")
	settings.add(r_status)
	settings.add(btn_back)

	return settings
