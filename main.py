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

def addevent():
	# Get event codes
	vals = getvals("event_codes")
	# Ask user to pick event code
	for entry in vals:
		print(entry[0],"-",entry[1])
	ids = [x[0] for x in vals]
	code = int(input("Which event code is this? "))
	if code not in ids:
		print("Code not valid.")
	else:
		# Get details of event (datetime, val, plant, notes)
		date = getdateuser()
		val = int(input("What is the value, only use whole numbers? "))
		plant = int(input("Which plant does this correspond to? "))
		notes = input("Please type any notes here: ")
		addentries.addevent("util/credentials", code, date.isoformat(), val, plant, notes)


def getdateuser():
	date = [int(x) for x in input("Please enter the year/month/day of the event: ").strip().split("/")]
	if date[0]<2000:
		date[0] += 2000
	return datetime.datetime(*date)

def getvals(table):
	mngr = sqlmanager.MySqlManager("lights")
	return mngr.export_table(table)

def lastwatered(plantno):
	mngr = sqlmanager.MySqlManager("lights")
	# load plant events for plantno with code 2
	rawweights = mngr.export_table("plant_events", condition = "WHERE code = 2 AND plant=" + plantno)

	tomorrow = None
	# Iterate through events from today to earliest date
	for row in rawweights[::-1]:
		if tomorrow:
			# if today > yesterday (aka the next term), return today
			if tomorrow > row[3]:
				print(row[2])
				return datetime.datetime.fromisoformat(row[2])
		tomorrow = row[3]
	return None

def printmenu():
	print("Menu:")
	print(" - add plant")
	print(" - add event")
	print(" - add event code")
	print(" - add sensor")
	print(" - get values")
	print(" - last watered")
	print(" - menu")
	print(" - exit")

while True:
	if uinp == "exit":
		exit()
	elif uinp == "menu":
		printmenu()
	elif uinp == "add plant":
		print("Adding plants")
		addplant()
	elif uinp == "add event":
		addevent()
	elif uinp == "add event code":
		addeventcode()
	elif uinp == "add sensor":
		print("Adding sensor")
		addsensor()
	elif uinp == "get values":
		table = input("Which table would you like the values from? ")
		for entry in getvals(table):
			print(entry)
	elif uinp == "last watered":
		plantno = input("Which plant would you like to know about? ")
		lastwatered(plantno)
	else:
		print("Sorry, that's not one of the menu options. To exit type exit")
	uinp = input("What would you like to do? ").lower()
