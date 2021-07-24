from util import sqlmanager
from decouple import config
import datetime

mngr = sqlmanager.MySqlManager(config('DB_NAME'))

def add_event():
    # Get event codes
    vals = mngr.export_table("event_codes")
    # Ask user to pick event code
    for entry in vals:
        print("\t", entry[0], "-", entry[1])
    ids = [x[0] for x in vals]
    code = int(input("Which event code is this? "))
    if code not in ids:
        print("Code not valid.")
    else:
		# Get details of event (datetime, val, plant, notes)
        usrinp = input("Type n if the event didn't happen today, or anything else for today: ")
        if usrinp == "n":
            date = [int(x) for x in input("Please enter the year/month/day of the event: ").strip().split("/")]
            if date[0] < 2000:
                date[0] += 2000
            date = datetime.datetime(*date)
        else:
            date = datetime.datetime.today()
        plant = int(input("Which plant does this correspond to? "))
        val = int(input("What is the value, only use whole numbers? "))
        notes = input("Please type any notes here: ")
        mngr.add_values("plant_events",
            ["code", "datetime", "val", "plant", "notes"],
            [code, date, val, plant, notes])
