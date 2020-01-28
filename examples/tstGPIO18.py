#!/usr/bin/python

# --------------------------------------------
# RPICM3 - Programma test Reset Cycle (GPIO18)
# --------------------------------------------

import RPi.GPIO as GPIO
import time
import os
import sys

# Pulisce lo schermo
os.system("clear")

# Disattiva warnings GPIO
GPIO.setwarnings(False)

# Imposta modalita' utilizzo GPIO
GPIO.setmode(GPIO.BCM)

# Definisce le linee GPIO
GPIO.setup(18, GPIO.OUT) # GPIO18

print("Start Reset Cycle demo!")
print("-----------------------")

print("Set GPIO18 --> Reset Cycle STARTED!")
GPIO.output(18,True)

try:

	timectr=0
	while (True):
		print("Time: " + str(timectr) + "s")
		time.sleep(1)
		timectr = timectr + 1

except KeyboardInterrupt:
	print "Program termination detected!"
except SystemExit:
	print "System exit detected!"
except:
	print("Error detected!")
finally:
	print("Program exit.")
	sys.stdout.flush()
	sys.exit(0)
