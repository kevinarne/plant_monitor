import time
import serial
import lightdbhandler as hndl

def read_light():
	with serial.Serial("/dev/ttyUSB0", 9600, timeout=10) as ser:
		entry = ser.readline()
		print(int(entry))
	return int(entry)
for x in range(5):
	try:
		with open("credentials","r") as f:
			usr, pwd = f.read().strip().split()
			break
	except:
		print("Credentials failed to load, please consult setup/README.md for instructions on setting up the mysql database credentials.")
		time.sleep(3)
		if x == 4:
			exit()

db = hndl.LightDBHandler("localhost", usr, pwd)

while True:
	entry = read_light()
	db.add_value(entry)	
	#usr = input("What would you like to do?")
	#if usr == "read sensor":
	#	
	#elif usr == "exit":
	#	break
	#else:
	#	print("I'm sorry, thats not a valid options. The valid options are:\n - read sensor\n - exit")
	time.sleep(10)
