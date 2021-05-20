import pymysql
#File for managing some basic mysql tasks in plainer English
class MySqlManager:
	def __init__(self, cred_path, db_name):
		self.db_name = db_name
		# Check for credentials
		try:
			with open(cred_path, "r") as f:
				self.username, self.pwd, self.host = f.read().strip().split("\n")
		except:
			print("Something went wrong loading the credentials, please check that the file exists and is formatted correctly")
			exit()
		# Check for database existence
		try:
			with pymysql.connect(host=self.host, user = self.username, password = self.pwd, database = self.db_name) as db:
				cur = db.cursor()
				print("Database connection made successfully.")
		except:
			print("Database", self.db_name, "not found. Creating now.")
			self.create_db(self.db_name)
			try:
				with pymysql.connect(host=self.host, user = self.username, password = self.pwd, database = self.db_name) as db:
					cur = db.cursor()
					print("Database connection made successfully.")
			except:
				print("Database connection still failed, check your credentials and the permissions of your database.")
				exit()

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
			pass
		else:
			for col in cols:
				query += ", " + col.to_str()
		query += ", PRIMARY KEY(" + primary.name + "))"
		print(query)
		try:
			self.execute_mysql(query,())
		except:
			print(tablename, "already exists.")

	def create_db(self, db_name):
		with pymysql.connect(host = self.host, user = self.username, password = self.pwd) as db:
			cur = db.cursor()
			print("Creating database")
			cur.execute("CREATE DATABASE " + db_name)

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
	def id_primary():
		return MySqlCol("id", "INT NOT NULL AUTO_INCREMENT")

class Table:
	def __init__(self):
		pass

if __name__ == "__main__":
	mngr = MySqlManager("credentials", "lights")
	user_inp = input("Would you like to create the needed databases and tables (y/n)?")
	if user_inp == "y":
		#Create database
		#Create light_vals table
		mngr.create_table("light_vals", MySqlCol.id_primary(), cols = [MySqlCol("val","INT"), MySqlCol("datetime","VARCHAR(30)")])
		#Create plants table
		mngr.create_table("plants", MySqlCol.id_primary(), cols=[MySqlCol("nickname", "VARCHAR(40)"),MySqlCol("notes","VARCHAR(200)")])
		#Create plant_events table
		mngr.create_table("plant_events", MySqlCol.id_primary(), cols = [MySqlCol("code","INT NOT NULL"), MySqlCol("datetime","VARCHAR(30)"), MySqlCol("val","INT"), MySqlCol("plant","INT"), MySqlCol("notes","VARCHAR(140)")])
		#Create event_codes table
		mngr.create_table("event_codes", MySqlCol.id_primary(), cols = [MySqlCol("description","VARCHAR(140)")])
		pass
