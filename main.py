import time
import serial
import lightdbhandler as hndl
#print([comport.device for comport in serial.tools.list_ports.comports()])
#com = input("Which COM port is the Arduino connected to?")
def read_light():
	with serial.Serial("/dev/ttyUSB0", 9600, timeout=10) as ser:
		entry = ser.readline()
		print(int(entry))
	return int(entry)
with open("credentials","r") as f:
	usr, pwd = f.read().strip().split()

db = hndl.LightDBHandler("localhost", usr, pwd)

while True:
	usr = input("What would you like to do?")
	if usr == "read sensor":
		entry = read_light()
		db.add_value(entry)
	elif usr == "exit":
		break
	#time.sleep(3)
