#!/bin/python
import datetime
import time

#set some vars
date = datetime.datetime.now()

print("\033[1;32m+-----------------------------------------+\033[0m")
print("\033[1;32m|\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|\033[0m")
print("\033[1;32m|-=[ \033[0m\033[1;35mAutomated CPU Temperature Monitor\033[0m\033[1;32m ]=-|\033[0m")
print("\033[1;32m|-------------=(\033[0;35m^C to quit\033[1;32m)=--------------|\033[0m")
print("\033[1;32m|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|\033[0m")
print("\033[1;32m+-----------------------------------------+\033[0m")

purple = "\033[1;35m"
ltpurple = "\033[0;35m"
green = "\033[1;32m"
red = "\033[1;31m"
orange = "\033[1;33m"
nocolour = "\033[0m"
info = "\033[1;35mCurrent Temperature:\033[0m"
format = "° Celsius"
datecolour = "\033[0;35m" #lighter weight purple
tempcolour = "\033[1;32m" #green

def getTemp():
	TEMP_FILE = open("/sys/class/thermal/thermal_zone0/temp", "r")
	TEMP_C = int(TEMP_FILE.read())/1000
	print(datecolour) #use colour for date
	print(datetime.datetime.now().isoformat(),nocolour)
	#Trying an if in here
	if TEMP_C < 70:
		print(info, tempcolour, TEMP_C, format, nocolour)
	elif TEMP_C >= 70:
		print(info, orange, TEMP_C, format, nocolour)
	elif TEMP_C >= 80:
		print(info, red, TEMP_C, format, nocolour)
	#print("\033[1;33mCurrent Temperature:\033[0m")
	#print(TEMP_C, end="", flush=True)
	#print("° Celsius \n")

while True:
	getTemp()
	time.sleep(5)

