# Main script to manage all user-facing activities like adding new plants,
# creating new event codes, adding manual events (like actual weights),
# pulling up visualizations of the data, etc
import addplants

uinp = input("What would you like to do? ").lower()

while True:
	if uinp == "exit":
		exit()
	elif uinp == "menu":
		print("Now I'll display the menu: ")
	elif uinp == "add plant":
		print("Adding plants")
		name = input("What would you like to call this plant? ")
		notes = input("Please type any notes about your plant here: ")
		addplants.addplant("util/credentials", name, notes)
	elif uinp == "add weight":
		print("Add weight")
	elif uinp == "add sensor":
		print("Adding sensor")

	else:
		print("Sorry, that's not one of the menu options. To exit type exit")
	uinp = input("What would you like to do? ").lower()
