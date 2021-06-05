from util import sqlmanager
#Add plants to database

def addplant(credpath, nickname, notes):
	mngr = sqlmanager.MySqlManager(credpath, "lights")
	mngr.add_values("plants", ["nickname", "notes"], [nickname, notes])

def addsensor(credpath, description, active, type, schedule, units, subscribed):
	mngr = sqlmanager.MySqlManager(credpath, "lights")
	mngr.add_values("sensors",
		["description","active","type","schedule","units","subscribed"],
		[description, active, type, schedule, units, subscribed])

def addeventcode(credpath, description):
	mngr = sqlmanager.MySqlManager(credpath, "lights")
	mngr.add_values("event_codes", ["description"], [description])

if __name__ == "__main__":
	user_inp = input("Would you like to add a plant [y/n]? ")
	if user_inp == "y":
	    name = input("What is the plant's name? ")
	    notes = input("Please type any notes about the plant and press enter. ")
	    mngr = sqlmanager.MySqlManager("util/credentials", "lights")
	    print(name,notes)
	    mngr.add_values("plants",["nickname","notes"], [name, notes])
