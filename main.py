# Main script to manage all user-facing activities like adding new plants,
# creating new event codes, adding manual events (like actual weights),
# pulling up visualizations of the data, etc
import addentries
import datetime
from util import sqlmanager
from util import addplant, addsensor, addeventcode, addevent
import matplotlib.pyplot as plt
import numpy as np
from decouple import config

mngr = sqlmanager.MySqlManager(config('DB_NAME'))

uinp = input("What would you like to do? ").lower()

class PlantEvent:
	def __init__(self, id, code, datetime, val, plant, notes):
		self.id = id
		self.code = code
		self.datetime = datetime
		self.val = val
		self.plant = plant
		self.notes = notes

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
		addplant.add_plant()
	elif uinp == "add event":
		addevent.add_event()
	elif uinp == "add event code":
		addeventcode.add_event_code()
	elif uinp == "add sensor":
		print("Adding sensor")
		addsensor.add_sensor()
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
