# Handler class for connections to the light table in the database
import pymysql

class LightDBHandler:
	entries = []
	def __init__(self, host, username, pwd):
		self.host = host
		self.username = username
		self.pwd = pwd
		print("LightDBHandler instantiated")
		#load data

def create_db(host, username, pwd):
	with pymysql.connect(host = host, user = username, password = pwd) as db:
		cur = db.cursor()
		print("Creating database")
		cur.execute("CREATE DATABASE lights")

def create_table(host, username, pwd, database, tablename):
	with pymysql.connect(host = host, user = username, password = pwd, database = database) as db:
		cur = db.cursor()
		print("Creating table")
		cur.execute("CREATE TABLE light_vals (id INT NOT NULL AUTO_INCREMENT, val VARCHAR(10) NOT NULL, PRIMARY KEY(id))")



if __name__ == "__main__":
	try:
		with open("credentials","r") as f:
			user, pwd = f.read().strip().split()
		dbhandler = LightDBHandler("localhost",user,pwd)

	except:
		print("No credentials found. Read /setup/README.md for formatting of credentials file.")
