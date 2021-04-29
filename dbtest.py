import pymysql

def create_db(host, username, pwd):
	with pymysql.connect(host = host, user = username, password = pwd) as db:
		cur = db.cursor()
		print("Do something")
		cur.execute("CREATE DATABASE lights")

def create_table(host, username, pwd, database, tablename):
	with pymysql.connect(host = host, user = username, password = pwd, database = database) as db:
		cur = db.cursor()
		print("Creating table")
		cur.execute("CREATE TABLE light_vals (id INT NOT NULL AUTO_INCREMENT, time VARCHAR(75) NOT NULL, val VARCHAR(10) NOT NULL, PRIMARY KEY(id))")
		
host = "localhost"

with open("credentials","r") as f:
	user, pwd = f.read().split() 

#create_db(host,user,pwd)
create_table(host, user, pwd, "lights", "lights")
