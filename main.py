# Main script to manage all user-facing activities like adding new plants,
# creating new event codes, adding manual events (like actual weights),
# pulling up visualizations of the data, etc
import addentries
import datetime
from util import sqlmanager
uinp = input("What would you like to do? ").lower()

def addplant():
	name = input("What would you like to call this plant? ")
	notes = input("Please type any notes about your plant here: ")
	addentries.addplant("util/credentials", name, notes)

def addsensor():
	description = input("Please describe this sensor: ")
	active = "y"
	type = input("What type of sensor is this (use correct id number)? ")
	units = input("What are the units of measurement? ")
	subscribed = input("Which plants are subscribed to this sensor (separate id #s by commas)? ")
	schedule = input("What schedule should this be polled at (use crontab notation)? ")
	addentries.addsensor("util/credentials", description, active, type, schedule, units, subscribed)

def addeventcode():
	description = input("Please enter a description (140 char max): ")
	if len(description) > 140:
		print("Description too long, truncating to 140")
		description = description[:139]
	addentries.addeventcode("util/credentials", description)

def getdateuser():
	date = [int(x) for x in input("Please enter the year/month/day of the event: ").strip().split("/")]
	if date[0]<2000:
		date[0] += 2000
	return datetime.datetime(*date)

while True:
	if uinp == "exit":
		exit()
	elif uinp == "menu":
		print("Menu:")
		print(" - add plant")
		print(" - add weight")
		print(" - add event")
		print(" - add event code")
		print(" - add sensor")
		print(" - get values")
		print(" - menu")
		print(" - exit")
	elif uinp == "add plant":
		print("Adding plants")
		addplant()
	elif uinp == "add weight":
		print("Add weight")
	elif uinp == "add event":
		# Get event codes
		# Ask user to pick event code
		# Get details of event (datetime, val, plant, notes)
		code = input("Which event code is this? ")
		date = getdateuser()
		val = input("What is the value? ")
		plant = input("Which plant does this correspond to? ")
		notes = input("Please type any notes here: ")
	elif uinp == "add event code":
		addeventcode()
	elif uinp == "add sensor":
		print("Adding sensor")
		addsensor()
	elif uinp == "get values":
		table = input("Which table would you like the values from? ")
		mngr = sqlmanager.MySqlManager("util/credentials","lights")
		vals = mngr.export_table(table)
		for entry in vals:
			print(entry)
	else:
		print("Sorry, that's not one of the menu options. To exit type exit")
	uinp = input("What would you like to do? ").lower()
