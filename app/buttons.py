from aiogram import types
from loader import db
from app.data import uz_countries

# This is inline keyboard will be showed when user send command /dashboard
def show_dashboard(user_id):
	groups = db.get_my_groups(user_id)
	dashboard = types.InlineKeyboardMarkup(row_width = 2)
	for i in groups:
		group_btn = types.InlineKeyboardButton(text = i[1], callback_data = f"group_id {i[0]}")
		dashboard.add(group_btn)

	startgroup = types.InlineKeyboardMarkup(text = "➕", url = "https://t.me/IslamReminderBot?startgroup=new")
	dashboard.add(startgroup)

	return dashboard


def show_group_settings(group_id, status_remind):
	settings = types.InlineKeyboardMarkup(row_width = 2)
	r_status = types.InlineKeyboardButton(text = f'Namoz vaqtini eslatish {status_remind}', callback_data = f'change_rStatus {group_id}')
	show_countries = types.InlineKeyboardButton(text = f'Mintaqani sozlash', callback_data = f'show_countries {group_id}')
	# set_audio = types.InlineKeyboardButton(text = f'Azon Ovozi', callback_data = f'show_audios {group_id}')
	# b_status = types.InlineKeyboardButton(text = f'Yozishni cheklash', callback_data = f'b_status')
	btn_back = types.InlineKeyboardMarkup(text = "⬅️ Orqaga", callback_data = "back_to_dashboard")
	settings.add(
		r_status, show_countries
		# set_audio, b_status
		)
	settings.add(btn_back)

	return settings


def show_audios(group_id, a_status):
	audios = db.get_azan_audios()
	audio_dashboard = types.InlineKeyboardMarkup(row_width = 2)
	for i in range(len(audios)):
		i += 1
		audio_btn = types.InlineKeyboardButton(text = f"{i} {a_status}", callback_data = f"audio_id {i}")
		audio_dashboard.add(audio_btn)

	random_mode = types.InlineKeyboardMarkup("Random", callback_data = f"set_audio_to_random_mode {group_id}")
	btn_back = types.InlineKeyboardMarkup(text = "⬅️ Orqaga", callback_data = f"back_to_settings {group_id}")
	audio_dashboard.add(random_mode)
	audio_dashboard.add(btn_back)

	return audio_dashboard


def get_indicator(group_id, country):
	flag = db.get_group_location(group_id)[0]
	if flag == country:
		return '✅'
	else:
		return ''

def show_countries(group_id):
	countries = types.InlineKeyboardMarkup(row_width = 4)
	for i in uz_countries:
		c_name = types.InlineKeyboardButton(text = f"{get_indicator(group_id, i.lower())} {i.title()}", callback_data = f"set_location {i.lower()},{group_id}")
		countries.insert(c_name)

	btn_back = types.InlineKeyboardMarkup(text = "⬅️ Orqaga", callback_data = f"back_to_settings {group_id}")
	countries.add(btn_back)

	return countries