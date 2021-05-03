import time
import serial
#print([comport.device for comport in serial.tools.list_ports.comports()])
#com = input("Which COM port is the Arduino connected to?")
def read_light():
	with serial.Serial("/dev/ttyUSB0", 9600, timeout=10) as ser:
		entry = ser.readline()
		print(int(entry))
	return entry
while True:
	usr = input("What would you like to do?")
	if usr == "read sensor":
		read_light()
	elif usr == "exit":
		break
	#time.sleep(3)
