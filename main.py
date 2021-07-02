# Main script to manage all user-facing activities like adding new plants,
# creating new event codes, adding manual events (like actual weights),
# pulling up visualizations of the data, etc
import addentries
import datetime
from util import sqlmanager
import matplotlib.pyplot as plt
import numpy as np

mngr = sqlmanager.MySqlManager("lights")

uinp = input("What would you like to do? ").lower()

class PlantEvent:
	def __init__(self, id, code, datetime, val, plant, notes):
		self.id = id
		self.code = code
		self.datetime = datetime
		self.val = val
		self.plant = plant
		self.notes = notes

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
		description = description[: 139]
	addentries.addeventcode("util/credentials", description)

def addevent():
	# Get event codes
	vals = getvals("event_codes")
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
			date = getdateuser()
		else:
			date = datetime.datetime.today()
		plant = int(input("Which plant does this correspond to? "))
		val = int(input("What is the value, only use whole numbers? "))
		notes = input("Please type any notes here: ")
		addentries.addevent("util/credentials", code, date.isoformat(), val, plant, notes)

def plantstatus(plant):
	vals = mngr.export_table("plant_events", condition = "WHERE code = 2 and plant = " + plant)
	# Traverse weight events
	max = 0
	min = 1000000
	wdates = []
	tomorrow = None
	print("Today's weight:", vals[len(vals)-1][3])
	for row in vals[: : -1]:
		if row[3] > max:
			max = row[3]
		if row[3] < min:
			min = row[3]
		if tomorrow:
			if row[3] < tomorrow:
				wdates.append(PlantEvent(
					row[0],
					row[1],
					datetime.datetime.fromisoformat(row[2][:19]),
					row[3],
					row[4],
					row[5]))
		tomorrow = row[3]
	x = []
	y = []
	for row in vals:
		# Add date to x
		x.append(datetime.datetime.fromisoformat(row[2][:19]).date().strftime("%m/%d"))
		# Add val to y
		y.append(int(row[3]) / 100)
	fig, ax = plt.subplots()
	ax.plot(x, y)

	ax.set(xlabel='Date', ylabel='Weight (oz)')
	plt.xticks([])
	plt.show()

	print("Last watered on ",wdates[0].datetime, "at a weight of",wdates[0].val)
	# Get average watering

def getdateuser():
	date = [int(x) for x in input("Please enter the year/month/day of the event: ").strip().split("/")]
	if date[0] < 2000:
		date[0] += 2000
	return datetime.datetime(*date)

def getvals(table):
	return mngr.export_table(table)

def getplants():
	return [(row[0], row[1]) for row in getvals("plants")]

def printmenu():
	print("Menu:")
	print(" - add plant")
	print(" - add event")
	print(" - add event code")
	print(" - add sensor")
	print(" - get values")
	print(" - plant status")
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
	elif uinp == "plant status":
		print("Available plants: ")
		for tup in getplants():
			print("\t", tup[0], "-", tup[1])
		plant = input("Which plant? ")
		plantstatus(plant)
	else:
		print("Sorry, that's not one of the menu options. To exit type exit")
	uinp = input("What would you like to do? ").lower()
