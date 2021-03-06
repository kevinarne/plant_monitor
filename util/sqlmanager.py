import pymysql
import decouple
#File for managing some basic mysql tasks in plainer English
class MySqlManager:
	"""
	Manages connections and queries with MySQL database.

	This is meant to be a step up  from pymysql's interface with the database into more human-readable language. It also handles pulling the database credentials from the environmental variables.
	"""
	def __init__(self, db_name):
		self.db_name = db_name
		# Check for database existence
		self.host = decouple.config('HOST_NAME')
		self.username = decouple.config('USER_NAME')
		self.pwd = decouple.config('PASSWORD')

		try:
			with pymysql.connect(host=self.host, user=self.username, password=self.pwd, database=self.db_name) as db:
				cur = db.cursor()
				#print("Database connection made successfully.")
		except:
			print("Database", self.db_name, "not found. Creating now.")
			self.create_db(self.db_name)
			try:
				with pymysql.connect(host=self.host, user=self.username, password=self.pwd, database=self.db_name) as db:
					cur = db.cursor()
					#print("Database connection made successfully.")
			except:
				print("Database connection still failed, check your credentials and the permissions of your database.")
				exit()

	def add_values(self, tablename, cols, values):
		"""
		Adds values to a table in the database.

		tablename - string name of the target table
		cols - list of strings containing the targeted column names
		values - list of corresponding column values, must match order of cols
		"""
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
		"""
		Executes a MySQL query with vals.

		Many of the other functions are wrappers for this one.
		query = string MySQL query
		vals = values to be added to the MySQL query
		"""
		with pymysql.connect(host=self.host, user=self.username, password=self.pwd, database=self.db_name) as db:
			cur = db.cursor()
			if len(vals) == 0:
				cur.execute(query)
			else:
				cur.execute(query, vals)
			db.commit()
			return cur.fetchall()

	def create_table(self, tablename, primary, cols=None):
		"""
		Creates a table in the database

		tablename - string name of the table
		primary - MySqlCol primary key
		cols - list of additional columns in MySqlCol form
		"""
		query = "CREATE TABLE " + tablename + " (" + primary.to_str()
		if cols == None:
			pass
		else:
			for col in cols:
				query += ", " + col.to_str()
		query += ", PRIMARY KEY(" + primary.name + "))"
		#print(query)
		try:
			self.execute_mysql(query, ())
		except:
			print(tablename, "already exists.")
	def create_db(self, db_name):
		"""
		Creates a database

		db_name - string name of the database
		"""
		with pymysql.connect(host=self.host, user=self.username, password=self.pwd) as db:
			cur = db.cursor()
			print("Creating database")
			cur.execute("CREATE DATABASE " + db_name)

	def export_table(self, table, condition=None):
		"""
		Exports all of the values from a given table.

		conditiions can be added to reduce the load on the database

		table - string name of the table
		condition - string containing the conditions appended to the query
		"""
		if not condition:
			condition = ""
		else:
			condition = " " + condition

		with pymysql.connect(host=self.host, user=self.username, password=self.pwd, database=self.db_name) as db:
			cur = db.cursor()
			cur.execute("SELECT * FROM " + table + condition)
			return cur.fetchall()

class MySqlCol:
	"""
	Class describing a MySQL column.
	"""
	def __init__(self, name, attrs):
		self.name = name
		self.attrs = attrs
	def to_str(self):
		return str(self.name + " " + self.attrs)
	def id_primary():
		return MySqlCol("id", "INT NOT NULL AUTO_INCREMENT")

if __name__ == "__main__":
	pass
