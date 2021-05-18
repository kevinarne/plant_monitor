import pymysql
#File for managing some basic mysql tasks in plainer English
class MySqlManager:
	def __init__(self, cred_path, db_name = None):
		print("initializing")
		#read the credentials file
		try:
			with open(cred_path, "r") as f:
				self.username, self.pwd, self.host = f.read().strip().split("\n")
		except:
			print("Something went wrong loading the credentials, please check that the file exists and is formatted correctly")
			exit()
		if db_name == None:
			self.if_no_db()
		else:
			self.db_name = db_name


	def add_value(self, value):
		print("Adding values")
		self.execute_mysql("INSERT INTO light_vals (datetime, val) VALUES (%s,%s)",(datetime.now().isoformat(),value))

	def execute_mysql(self, query, vals):
		with pymysql.connect(host = self.host, user = self.username, password = self.pwd, database = self.db_name) as db:
			cur = db.cursor()
			if len(vals) == 0:
				cur.execute(query)
			else:
				cur.execute(query,vals)
			db.commit()

	def create_table(self, tablename, primary, cols = None):
		query = "CREATE TABLE " + tablename + " (" + primary.to_str()
		if cols == None:
			query += ", PRIMARY KEY(" + primary.name + "))"
			print(query)
		else:
			for num, col in enumerate(cols):
				if num == 0:
					pass
				else:
					pass
				print(num)
				print(col.to_str())
		#query = "CREATE TABLE " + tablename + " (id INT NOT NULL AUTO_INCREMENT, val INT NOT NULL, datetime VARCHAR(30) NOT NULL, PRIMARY KEY(id))"
		#self.execute_mysql(query,())

	def create_db(self, db_name):
		with pymysql.connect(host = self.host, user = self.username, password = self.pwd) as db:
			cur = db.cursor()
			print("Creating database")
			cur.execute("CREATE DATABASE " + db_name)

	def if_no_db(self):
		user_input = input("Please enter your database name or enter 0 if you need to create one")
		if user_input == "0":
			db_name = input("Please enter the desired databased name: ")
			self.db_name = db_name
			self.create_db(db_name)
		else:
			self.db_name = user_input

	def export_table(self, table):
		with pymysql.connect(host = self.host, user = self.username, password = self.pwd, database = self.db_name) as db:
			cur = db.cursor()
			cur.execute("SELECT * FROM " + table)
			return cur.fetchall()

class MySqlCol:
	def __init__(self, name, attrs):
		self.name = name
		self.attrs = attrs
	def to_str(self):
		return str(self.name + " " + self.attrs)

if __name__ == "__main__":
	mngr = MySqlManager("credentials", db_name = "lights")
	mngr.create_table("test_table", MySqlCol("id","ATTR1"), cols=[MySqlCol("test2","ATTR2"),MySqlCol("test3","ATTR3")])
	pass
