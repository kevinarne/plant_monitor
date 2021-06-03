import sqlmanager as my
# Read all data from existing database
mngr = my.MySqlManager("credentials", "lights")
entries = mngr.export_table("light_vals")
# Iterate through entries
plants = [2,3,4,5]
for entry in entries:
    print(entry)
    for plant in plants:
        cols = ["code","datetime","val","plant","notes"]
        vals = [1,entry[2],entry[1],plant,"From sensor 1"]
        mngr.add_values("plant_events", cols, vals)
        print(vals)
