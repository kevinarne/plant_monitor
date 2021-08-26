# Pull data from the database and put it into simple csv formats.
from sqlmanager import MySqlManager
mngr = MySqlManager("lights")

# Pull plant list
plants = mngr.export_table("plants")
for plant in plants:
    print(f"{plant[0]} - {plant[1]}")
# Ask user which plant
plant_num = int(input("Which plant number do you want data from? \n"))
if plant_num in [plant[0] for plant in plants]:
    print("Correct input")
else:
    print("Incorrect input")
    exit()

# Pull event types
event_codes = mngr.export_table("event_codes")
for code in event_codes:
    print(f"{code[0]} - {code[1]}")
# Ask user which event type
event_num = int(input("Which event number do you want data from? \n"))
if event_num in [code[0] for code in event_codes]:
    print("Correct input")
else:
    print("Incorrect input")
    exit()

# Pull date and value for the event type chosen
query = f"SELECT datetime, val FROM plant_events WHERE plant={plant_num} AND code={event_num}"
vals = mngr.execute_mysql(query,[])

filename = input("What would you like to name this file?\n")

with open(filename+".csv", "a") as f:
    for val in vals:
        f.write(f"{val[0][0:19]}, {val[1] / 100}\n")
