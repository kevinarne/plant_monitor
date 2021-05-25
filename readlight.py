import serial
import datetime
from util import sqlmanager

def read_light():
	with serial.Serial("/dev/ttyUSB0", 9600, timeout=10) as ser:
		entry = ser.readline()
		print(int(entry))
	return int(entry)
	
if __name__ == "__main__":
	try:
		with open("scripts/lights/credentials","r") as f:
			usr, pwd, host = f.read().strip().split()
	except:
		print("Credentials failed to load, please consult setup/README.md for instructions on setting up the mysql database credentials.")
		with open("logs","a") as f:
			f.write("Failed to load database\n")

	mngr = sqlmanager.MySqlManager("scripts/lights/credentials","lights")

	entry = read_light()

	mngr.add_values("light_vals", ["val","datetime"], [entry, datetime.now().isoformat()])
