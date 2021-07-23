from util import sqlmanager
from decouple import config

def add_plant():
    mngr = sqlmanager.MySqlManager(config('DB_NAME'))

    name = input("What would you like to call this plant? ")
    notes = input("Please type any notes about your plant here: ")
    mngr.add_values("plants", ["nickname", "notes"], [name, notes])

if __name__ == "__main__":
    add_plant()
