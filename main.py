import serial
#print([comport.device for comport in serial.tools.list_ports.comports()])
#com = input("Which COM port is the Arduino connected to?")
while True:
	with serial.Serial("/dev/ttyUSB0", 9600, timeout=10) as ser:
		entry = ser.readline()
		print(entry)
	usr = input("Would you like to continue?")
	if usr == "no":
		break
	
