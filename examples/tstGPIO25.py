#!/usr/bin/python

# ----------------------------------------------------
# RPICM3 - Programma di esempio controllo stato GPIO25
# ----------------------------------------------------

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

# Definisce le linee GPIO come uscite
GPIO.setup(25, GPIO.IN) # O12

try:
	
	while (True):

		time.sleep(0.1)
		
		if (GPIO.input(25) == 1):
			print("P1: premuto")
		else:
			print("P1: non premuto")
		
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
