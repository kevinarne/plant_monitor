from util import sqlmanager
from decouple import config

mngr = sqlmanager.MySqlManager(config('DB_NAME'))

def add_sensor():
    description = input("Please describe this sensor: ")
    active = "y"
    type = input("What type of sensor is this (use correct id number)? ")
    units = input("What are the units of measurement? ")
    subscribed = input("Which plants are subscribed to this sensor (separate id #s by commas)? ")
    schedule = input("What schedule should this be polled at (use crontab notation)? ")
    mngr.add_values(
        "sensors",
		["description","active","type","schedule","units","subscribed"],
		[description, active, type, schedule, units, subscribed])

if __name__ == "__main__":
    add_sensor()
