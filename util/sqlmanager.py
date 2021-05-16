#File for managing some basic mysql tasks in plainer English

def execute_mysql(self, query, vals):
	with pymysql.connect(host = self.host, user = self.username, password = self.pwd, database = "lights") as db:
		cur = db.cursor()
		if len(vals) == 0:
			cur.execute(query)
		else:
			cur.execute(query,vals)
		db.commit()

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
