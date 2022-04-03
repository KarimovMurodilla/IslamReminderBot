import datetime
import sqlite3 as sql


class Database:
	def __init__(self, db_file):
		"""Initialization"""
		self.con = sql.connect(db_file)
		self.cur = self.con.cursor()

	# For users table
	def checkUser(self, user_id):
		"""
		We check the user in the database, if the user is not in the users table, 
		then we will register it in the database.
		"""
		with self.con:
			user = self.cur.execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,)).fetchone()

			if not user:
				self.cur.execute("INSERT INTO users (user_id, date_reg) VALUES (?, ?)", (user_id, datetime.datetime.today()))
				self.con.commit()

			return user

	# For groups table
	def get_data_from_group_id(self, group_id):
		"""
		Get all data where group_id == group_id.
		"""
		with self.con:
			response = self.cur.execute("SELECT * FROM groups WHERE group_id = ?", (group_id,)).fetchone()

		return response

	def reg_new_group(self, user_id, group_id, group_title):
		"""
		Register new group_id, group_title and 
		date of registration with user_id in table groups.
		"""
		with self.con:
			chat = self.cur.execute("SELECT group_id FROM groups WHERE group_id = ?", (group_id,)).fetchone()

			if not chat:
				self.cur.execute("INSERT INTO groups (user_id, group_id, group_title, date_reg) VALUES (?, ?, ?, ?)", (user_id, group_id, group_title, datetime.datetime.today()))
				self.con.commit()

	def get_my_groups(self, user_id):
		"""
		Returns the ids of the groups added by the user
		"""
		with self.con:
			group_ids = self.cur.execute("SELECT group_id, group_title FROM groups WHERE user_id = ?", (user_id,)).fetchall()

		return group_ids


	def delete_group(self, group_id):
		"""
		Removing a group from the database is performed 
		only when the user removes the bot from the group.
		"""
		with self.con:
			self.cur.execute("DELETE FROM groups WHERE group_id = ?", (group_id,))
			self.con.commit()

	def update_rStatus(self, group_id, r_status):
		"""
		Updates the rstatus field
		"""
		with self.con:
			self.cur.execute("UPDATE groups SET r_status = ? WHERE group_id = ?	", (r_status, group_id,))
			self.con.commit()

	def get_enabled_rstatuses(self):
		"""
		Get group ids where enabled remind statuses.
		"""
		with self.con:
			response = self.cur.execute("SELECT group_id FROM groups WHERE r_status = '🟢'").fetchall()

		return response

	def get_azan_audios(self):
		"""
		Getting azan audios file_id.
		"""
		with self.con:
			response = self.cur.execute("SELECT file_id FROM azan_audios").fetchall()

		return response

	def set_location(self, group_id, country_name):
		"""This method called when user wants to set his group location"""
		with self.con:
			self.cur.execute("UPDATE groups SET group_location = ? WHERE group_id = ?", (country_name, group_id,))
			self.con.commit()

	def get_group_location(self, group_id):
		"""This method returns group location"""
		with self.con:
			response = self.cur.execute("SELECT group_location FROM groups WHERE group_id = ?", (group_id,)).fetchone()
			
		return response

	def get_group_id_of_country(self, group_location):
		"""
		This method returns id of called country.
		Returns group_id if remind status is enabled
		"""
		with self.con:
			response = self.cur.execute("SELECT group_id FROM groups WHERE group_location = ? AND r_status = '🟢'", (group_location,)).fetchone()
			
		return response