import datetime
import sqlmanager

def postval(date, plant, val):
    mngr = sqlmanager.MySqlManager("lights")
    mngr.add_values("plant_events",
        ["code", "datetime", "val", "plant", "notes"],
        [2, date.isoformat(), val, plant, "In ounces * 100"])


# Open file
with open("plantweights.csv", "r") as f:
    # Iterate through rows
    for entry in f:
        entrylist = entry.strip().split(',')
        # Parse dates
        mdy = entrylist[0].split("/")
        print(mdy)
        date = datetime.datetime(int(mdy[2]), int(mdy[0]), int(mdy[1]))
        # Add each of the four plant weights for each date
        postval(date, 2, int(float(entrylist[1])*100))
        postval(date, 3, int(float(entrylist[2])*100))
        postval(date, 4, int(float(entrylist[3])*100))
        postval(date, 5, int(float(entrylist[4])*100))
