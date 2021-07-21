from sqlmanager import MySqlManager
import datetime
from decouple import config
import smtplib, ssl

port = 465

mngr = MySqlManager(config('DB_NAME'))

SENSOR_ACTIVE_COL = 2
ID_COL = 0
PLANT_EVENT_DATETIME_COL = 2

# Get the list of sensors from the database
sensors = mngr.export_table("sensors")

sensor_status_string = ""

# For each sensor, find the most recent entry
for row in sensors:
    if row[SENSOR_ACTIVE_COL] == "y":
        # Query the database for the most recent entry from each sensor
        query = "SELECT * FROM plant_events WHERE source='s" + str(row[ID_COL]) + "' ORDER BY id DESC LIMIT 1"

        # Convert the datetime column of that entry to the proper iso string
        iso_string = mngr.execute_mysql(query,[])[0][PLANT_EVENT_DATETIME_COL].split(".")[0]

        most_recent = datetime.datetime.fromisoformat(iso_string)
        today = datetime.datetime.today()

        print(f"Time since sensor {row[ID_COL]} last reported: {today - most_recent}")

        if today - most_recent > datetime.timedelta(days=1):
            sensor_status_string += f"s{row[ID_COL]}\n"

if len(sensor_status_string) > 0:
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(config('EMAIL_USER'), config('EMAIL_PASS'))
        message = sensor_status_string
        server.sendmail(config('EMAIL_USER'), config('MAIN_EMAIL'), "Subject: Sensor down\n\nThe following sensors have not reported in over a day:\n"+sensor_status_string)
