EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Device:R_PHOTO R1
U 1 1 60E4F4D5
P 4300 4000
F 0 "R1" H 4370 4046 50  0000 L CNN
F 1 "R_PHOTO" H 4370 3955 50  0000 L CNN
F 2 "" V 4350 3750 50  0001 L CNN
F 3 "~" H 4300 3950 50  0001 C CNN
	1    4300 4000
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0101
U 1 1 60E4FE8A
P 4300 4650
F 0 "#PWR0101" H 4300 4400 50  0001 C CNN
F 1 "GND" H 4305 4477 50  0000 C CNN
F 2 "" H 4300 4650 50  0001 C CNN
F 3 "" H 4300 4650 50  0001 C CNN
	1    4300 4650
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0102
U 1 1 60E5063A
P 1950 3050
F 0 "#PWR0102" H 1950 2900 50  0001 C CNN
F 1 "VCC" H 1965 3223 50  0000 C CNN
F 2 "" H 1950 3050 50  0001 C CNN
F 3 "" H 1950 3050 50  0001 C CNN
	1    1950 3050
	1    0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR0103
U 1 1 60E513CB
P 4300 3700
F 0 "#PWR0103" H 4300 3550 50  0001 C CNN
F 1 "+3.3V" H 4315 3873 50  0000 C CNN
F 2 "" H 4300 3700 50  0001 C CNN
F 3 "" H 4300 3700 50  0001 C CNN
	1    4300 3700
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small_US R2
U 1 1 60E51DCF
P 4300 4400
F 0 "R2" H 4368 4446 50  0000 L CNN
F 1 "R_Small_US" H 4368 4355 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 4300 4400 50  0001 C CNN
F 3 "~" H 4300 4400 50  0001 C CNN
	1    4300 4400
	1    0    0    -1  
$EndComp
Wire Wire Line
	4300 3700 4300 3850
Wire Wire Line
	4300 4500 4300 4650
$Comp
L Device:Battery_Cell BT1
U 1 1 60E5549B
P 1950 3350
F 0 "BT1" H 2068 3446 50  0000 L CNN
F 1 "Battery_Cell" H 2068 3355 50  0000 L CNN
F 2 "TestPoint:TestPoint_2Pads_Pitch2.54mm_Drill0.8mm" V 1950 3410 50  0001 C CNN
F 3 "~" V 1950 3410 50  0001 C CNN
	1    1950 3350
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0104
U 1 1 60E5641E
P 1950 3550
F 0 "#PWR0104" H 1950 3300 50  0001 C CNN
F 1 "GND" H 1955 3377 50  0000 C CNN
F 2 "" H 1950 3550 50  0001 C CNN
F 3 "" H 1950 3550 50  0001 C CNN
	1    1950 3550
	1    0    0    -1  
$EndComp
Wire Wire Line
	1950 3050 1950 3150
Wire Wire Line
	1950 3450 1950 3550
$Comp
L Sensor:DHT11 U1
U 1 1 60F0CFA4
P 4300 2350
F 0 "U1" H 4056 2396 50  0000 R CNN
F 1 "DHT11" H 4056 2305 50  0000 R CNN
F 2 "Sensor:Aosong_DHT11_5.5x12.0_P2.54mm" H 4300 1950 50  0001 C CNN
F 3 "http://akizukidenshi.com/download/ds/aosong/DHT11.pdf" H 4450 2600 50  0001 C CNN
	1    4300 2350
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small_US R3
U 1 1 60F0DEE6
P 4700 2150
F 0 "R3" H 4768 2196 50  0000 L CNN
F 1 "R_Small_US" H 4768 2105 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 4700 2150 50  0001 C CNN
F 3 "~" H 4700 2150 50  0001 C CNN
	1    4700 2150
	1    0    0    -1  
$EndComp
Wire Wire Line
	4600 2350 4700 2350
Wire Wire Line
	4700 2350 4700 2250
Wire Wire Line
	4700 2050 4700 1900
Wire Wire Line
	4700 1900 4500 1900
Wire Wire Line
	4500 1900 4500 1750
Wire Wire Line
	4300 2050 4300 1900
Wire Wire Line
	4300 1900 4500 1900
Connection ~ 4500 1900
$Comp
L power:+3.3V #PWR0105
U 1 1 60F0F603
P 4500 1750
F 0 "#PWR0105" H 4500 1600 50  0001 C CNN
F 1 "+3.3V" H 4515 1923 50  0000 C CNN
F 2 "" H 4500 1750 50  0001 C CNN
F 3 "" H 4500 1750 50  0001 C CNN
	1    4500 1750
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0106
U 1 1 60F0FB1F
P 4300 2750
F 0 "#PWR0106" H 4300 2500 50  0001 C CNN
F 1 "GND" H 4305 2577 50  0000 C CNN
F 2 "" H 4300 2750 50  0001 C CNN
F 3 "" H 4300 2750 50  0001 C CNN
	1    4300 2750
	1    0    0    -1  
$EndComp
Wire Wire Line
	4300 2650 4300 2750
$Comp
L lightSensorESP32:ESP32-BO U2
U 1 1 60F165BF
P 6750 3150
F 0 "U2" H 6725 4165 50  0000 C CNN
F 1 "ESP32-BO" H 6725 4074 50  0000 C CNN
F 2 "lightSensorESP32:ESP32-BO" H 6700 3200 50  0001 C CNN
F 3 "" H 6700 3200 50  0001 C CNN
	1    6750 3150
	1    0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR0107
U 1 1 60F18BB9
P 6100 2350
F 0 "#PWR0107" H 6100 2200 50  0001 C CNN
F 1 "+3.3V" H 6115 2523 50  0000 C CNN
F 2 "" H 6100 2350 50  0001 C CNN
F 3 "" H 6100 2350 50  0001 C CNN
	1    6100 2350
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0108
U 1 1 60F19056
P 5900 2350
F 0 "#PWR0108" H 5900 2200 50  0001 C CNN
F 1 "VCC" H 5915 2523 50  0000 C CNN
F 2 "" H 5900 2350 50  0001 C CNN
F 3 "" H 5900 2350 50  0001 C CNN
	1    5900 2350
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0109
U 1 1 60F19A3C
P 7500 4350
F 0 "#PWR0109" H 7500 4100 50  0001 C CNN
F 1 "GND" H 7505 4177 50  0000 C CNN
F 2 "" H 7500 4350 50  0001 C CNN
F 3 "" H 7500 4350 50  0001 C CNN
	1    7500 4350
	1    0    0    -1  
$EndComp
Wire Wire Line
	7200 4200 7500 4200
Wire Wire Line
	7500 4200 7500 4350
Wire Wire Line
	7200 4100 7500 4100
Wire Wire Line
	7500 4100 7500 4200
Connection ~ 7500 4200
Wire Wire Line
	6100 2350 6100 2400
Wire Wire Line
	6100 2400 6250 2400
Wire Wire Line
	5900 2350 5900 2500
Wire Wire Line
	5900 2500 6250 2500
Wire Wire Line
	4700 2350 4800 2350
Connection ~ 4700 2350
Wire Wire Line
	6250 3000 6050 3000
Wire Wire Line
	6250 3100 6050 3100
Text GLabel 6050 3100 0    50   Input ~ 0
LGHT
Text GLabel 6050 3000 0    50   Input ~ 0
DHT
Text GLabel 4800 2350 2    50   Input ~ 0
DHT
Wire Wire Line
	4300 4150 4300 4200
Wire Wire Line
	4300 4200 4650 4200
Connection ~ 4300 4200
Wire Wire Line
	4300 4200 4300 4300
Text GLabel 4650 4200 2    50   Input ~ 0
LGHT
$EndSCHEMATC
