from sqlmanager import MySqlManager
import datetime

mngr = MySqlManager("lights")

SENSOR_ACTIVE_COL = 2
ID_COL = 0
PLANT_EVENT_DATETIME_COL = 2

# Get the list of sensors from the database
sensors = mngr.export_table("sensors")

# For each sensor, find the most recent entry
for row in sensors:
    if row[SENSOR_ACTIVE_COL] == "y":
        query = "SELECT * FROM plant_events WHERE source='s" + str(row[ID_COL]) + "' ORDER BY id DESC LIMIT 1"
        # Get the first row (only row) and the datetime column, removing anyhing after the decimal
        rawdata = mngr.execute_mysql(query,[])[0][PLANT_EVENT_DATETIME_COL].split(".")[0]

        # Remove the PD from PDT if it exists
        if len(rawdata) == 21:
            rawdata = rawdata[:10] + rawdata[12:]

        mostrecent = datetime.datetime.fromisoformat(rawdata)
        today = datetime.datetime.today()
        print("Time since last reported:", today - mostrecent)
