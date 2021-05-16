import mysql.connector
from datetime import datetime

# Get credentials
try:
    with open("credentials", "r") as f:
        hostname, username, pwd = f.read().strip().split("\n")
except:
    print("Credentials failed to load")
    exit()

with mysql.connector.connect(host=hostname, user=username, password=pwd, database="lights") as db:
    cur = db.cursor()
    cur.execute("SELECT * FROM light_vals;")
    data = cur.fetchall()
    with open("db.csv","a") as f:
        for entry in data:
            f.write(str(entry[0]) + "," + str(entry[1]) + "," + str(entry[2]) + "\n")
