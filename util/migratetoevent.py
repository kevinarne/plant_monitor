import sqlmanager as my
# Read all data from existing database
mngr = my.MySqlManager("credentials", "lights")
entries = mngr.export_table("light_vals")
# Iterate through entries
for entry in entries:
    print(entry)
# Add to event table for each plant (which means 4x entries for each light reading)
