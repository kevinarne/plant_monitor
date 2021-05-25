import sys
import serial
from datetime import datetime
from util import sqlmanager

try:
	cred_path = sys.argv[1]
	print(cred_path)
except:
	print("No credential path supplied.")
	exit()

def read_light():
	with serial.Serial("/dev/ttyUSB0", 9600, timeout=10) as ser:
		entry = ser.readline()
		print(int(entry))
	return int(entry)
	
if __name__ == "__main__":
	try:
	#"scripts/lights/credentials"
		with open(cred_path,"r") as f:
			usr, pwd, host = f.read().strip().split()
			print(usr,pwd,host)
	except:
		print("Credentials failed to load, please consult setup/README.md for instructions on setting up the mysql database credentials.")
		with open("logs","a") as f:
			f.write("Failed to load database\n")

	mngr = sqlmanager.MySqlManager(cred_path,"lights")

	entry = read_light()

	mngr.add_values("light_vals", ["val","datetime"], [entry, datetime.now().isoformat()])
