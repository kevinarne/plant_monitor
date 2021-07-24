from util import sqlmanager
from decouple import config

mngr = sqlmanager.MySqlManager(config('DB_NAME'))

def add_event_code():
    description = input("Please enter a description (140 char max): ")
    if len(description) > 140:
        print("Description too long, truncating to 140")
        description = description[: 139]
    mngr.add_values("event_codes", ["description"], [description])

if __name__ == "__main__":
    add_event_code()
