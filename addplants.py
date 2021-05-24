from util import sqlmanager
#Add plants to database
user_inp = input("Would you like to add a plant [y/n]? ")
if user_inp == "y":
    name = input("What is the plant's name? ")
    notes = input("Please type any notes about the plant and press enter. ")
    mngr = sqlmanager.MySqlManager("util/credentials", "lights")
    print(name,notes)
    mngr.add_values("plants",["nickname","notes"], [name, notes])
