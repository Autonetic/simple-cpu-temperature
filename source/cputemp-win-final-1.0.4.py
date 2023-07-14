import datetime
import time
import colorama
import clr
clr.AddReference(r'OpenHardwareMonitorLib')
#clr.AddReference(r'C:\Users\Autonetix\Documents\python\cputemp\cputemp-1.0.3\OpenHardwareMonitorLib') 
# e.g. clr.AddReference(r'OpenHardwareMonitor/OpenHardwareMonitorLib'), without .dll

from colorama import just_fix_windows_console
from OpenHardwareMonitor.Hardware import Computer

just_fix_windows_console()

print("\033[1;32m+-----------------------------------------+\033[0m")
print("\033[1;32m|\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|\033[0m")
print("\033[1;32m|-=[ \033[0m\033[1;35mAutomated CPU Temperature Monitor\033[0m\033[1;32m ]=-|\033[0m")
print("\033[1;32m|-------------=(\033[0;35m^C to quit\033[1;32m)=--------------|\033[0m")
print("\033[1;32m|/\/\/\/\/\/Coded@ Autonetix.co/\/\/\/\/\/|\033[0m")
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

c = Computer()
c.CPUEnabled = True # get the Info about CPU
c.GPUEnabled = True # get the Info about GPU
c.Open()
while True:
    for a in range(0, len(c.Hardware[0].Sensors)):
        # print(c.Hardware[0].Sensors[a].Identifier)
        if "/temperature" in str(c.Hardware[0].Sensors[a].Identifier):
            print(datecolour) #use colour for date
            print(datetime.datetime.now().isoformat(),nocolour)
            #Trying an if in here
            if c.Hardware[0].Sensors[a].get_Value() < 70:
                print(info, tempcolour, c.Hardware[0].Sensors[a].get_Value(), format, nocolour)
            elif c.Hardware[0].Sensors[a].get_Value() >= 70:
                print(info, orange, c.Hardware[0].Sensors[a].get_Value(), format, nocolour)
            elif c.Hardware[0].Sensors[a].get_Value() >= 80:
                print(info, red, c.Hardware[0].Sensors[a].get_Value(), format, nocolour)
            c.Hardware[0].Update()
            time.sleep(5)