import sqlmanager
import os
# Get tables to be backed up
tables = ["plant_events", "plants", "event_codes", "sensors"]
mngr = sqlmanager.MySqlManager("lights")

for table in tables:
    # Pull existing database
    data = mngr.export_table(table)
    with open("backups/"+ table + "temp.csv","a") as f:
        for row in data:
            # Write to temp file
            converted = [str(x) for x in row]
            f.write(",".join(converted) + "\n")

    # Delete previous file
    delcommand = "del /f backups\\" + table + ".csv"
    os.system(delcommand)
    # Rename temp file
    renamecommand = "rename backups\\" + table + "temp.csv " + table + ".csv"
    os.system(renamecommand)
