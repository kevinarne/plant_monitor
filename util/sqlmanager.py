import pymysql
import decouple
#File for managing some basic mysql tasks in plainer English
class MySqlManager:
	def __init__(self, db_name):
		self.db_name = db_name
		# Check for database existence
		self.host = decouple.config('HOST_NAME')
		self.username = decouple.config('USER_NAME')
		self.pwd = decouple.config('PASSWORD')

		try:
			with pymysql.connect(host=self.host, user = self.username, password = self.pwd, database = self.db_name) as db:
				cur = db.cursor()
				#print("Database connection made successfully.")
		except:
			print("Database", self.db_name, "not found. Creating now.")
			self.create_db(self.db_name)
			try:
				with pymysql.connect(host=self.host, user = self.username, password = self.pwd, database = self.db_name) as db:
					cur = db.cursor()
					#print("Database connection made successfully.")
			except:
				print("Database connection still failed, check your credentials and the permissions of your database.")
				exit()

	def add_values(self, tablename, cols, values):
		try:
			query = "INSERT INTO " + tablename + " ("
			for n, col in enumerate(cols):
				if n == len(cols) - 1:
					query += col
				else:
					query += col + ", "
			query += ") VALUES (" + (len(cols)-1) * "%s," + " %s)"
			self.execute_mysql(query, values)
		except:
			print("Something went wrong adding the values to the table. Make sure you provided the correct table name and values for that table. You may not have the appropriate permissions either.")

	def execute_mysql(self, query, vals):
		with pymysql.connect(host = self.host, user = self.username, password = self.pwd, database = self.db_name) as db:
			cur = db.cursor()
			if len(vals) == 0:
				cur.execute(query)
			else:
				cur.execute(query, vals)
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

	def export_table(self, table, condition = None):
		if not condition:
			condition = ""
		else:
			condition = " " + condition

		with pymysql.connect(host = self.host, user = self.username, password = self.pwd, database = self.db_name) as db:
			cur = db.cursor()
			cur.execute("SELECT * FROM " + table + condition)
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
	def __init__(self, primary, cols):
		self.primary = MySqlCol.id_primary()
		self.cols = []
	def get_primary(self):
		pass
	def get_cols(self):
		pass

def createtables(dbname):
	mngr = MySqlManager(dbname)
	#Create plants table
	mngr.create_table("plants", MySqlCol.id_primary(), cols=[MySqlCol("nickname", "VARCHAR(40)"),
		MySqlCol("notes","VARCHAR(200)")])
	#Create plant_events table
	mngr.create_table("plant_events", MySqlCol.id_primary(), cols = [MySqlCol("code","INT NOT NULL"),
		MySqlCol("datetime","VARCHAR(30)"),
		MySqlCol("val","INT"),
		MySqlCol("plant","INT"),
		MySqlCol("notes","VARCHAR(140)")])
	#Create event_codes table
	mngr.create_table("event_codes", MySqlCol.id_primary(), cols = [MySqlCol("description","VARCHAR(140)")])
	#Create sensors table
	mngr.create_table("sensors", MySqlCol.id_primary(), cols = [MySqlCol("description","VARCHAR(140)"),
		MySqlCol("active","VARCHAR(1)"),
		MySqlCol("type","INT"),
		MySqlCol("schedule","VARCHAR(20)"),
		MySqlCol("units","VARCHAR(20)"),
		MySqlCol("subscribed","VARCHAR(30)")])

if __name__ == "__main__":
	user_inp = input("Would you like to create the needed databases and tables (y/n)?")
	if user_inp == "y":
		createtables("lights")
