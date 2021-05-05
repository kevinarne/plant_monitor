# Handler class for connections to the light table in the database
import pymysql
from datetime import datetime

class LightDBHandler:
	entries = []
	def __init__(self, host, username, pwd):
		self.host = host
		self.username = username
		self.pwd = pwd
		print("LightDBHandler instantiated")

	def add_value(self, value):
		print("Adding values")
		self.execute_mysql("INSERT INTO light_vals (datetime, val) VALUES (%s,%s)",(datetime.now().isoformat(),value))

	def execute_mysql(self, query, vals):
		with pymysql.connect(host = self.host, user = self.username, password = self.pwd, database = "lights") as db:
			cur = db.cursor()
			if len(vals) == 0:
				cur.execute(query)
			else:
				cur.execute(query,vals)
			db.commit()

	def create_table(self, tablename):
		query = "CREATE TABLE " + tablename + " (id INT NOT NULL AUTO_INCREMENT, val INT NOT NULL, datetime VARCHAR(30) NOT NULL, PRIMARY KEY(id))"
		self.execute_mysql(query,())

	def create_db(host, username, pwd):
		with pymysql.connect(host = host, user = username, password = pwd) as db:
			cur = db.cursor()
			print("Creating database")
			cur.execute("CREATE DATABASE lights")




if __name__ == "__main__":
	usr_inp = input("Would you like to test the adding?")
	if usr_inp == "yes":
		try:
			with open("credentials","r") as f:
				user, pwd = f.read().strip().split()
		except:
			print("No credentials found. Read /setup/README.md for formatting of credentials file.")
			exit()
		dbhandler = LightDBHandler("localhost",user,pwd)
		dbhandler.create_table("light_vals")
		dbhandler.add_value(984)
	print("Exiting")
