from sqlmanager import MySqlManager

mngr = MySqlManager("lights")

# Get the list of sensors from the database
sensors = mngr.export_table("sensors")

# For each sensor, find the most recent entry
for row in sensors:
    if row[2] == "y":
        query = "SELECT * FROM plant_events WHERE source='s" + str(row[0]) + "' ORDER BY id DESC LIMIT 1"
        mostrecent = mngr.execute_mysql(query,[])
        print(mostrecent)
