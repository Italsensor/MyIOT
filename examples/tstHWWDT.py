#!/usr/bin/python

# --------------------------------------------
# RPICM3 - Programma test utilizzo watchdog
# --------------------------------------------

import RPi.GPIO as GPIO
import time
import os
import sys


try:
	# Pulisce lo schermo
	os.system("clear")

	# Disattiva warnings GPIO
	GPIO.setwarnings(False)

	# Imposta modalita' utilizzo GPIO
	GPIO.setmode(GPIO.BCM)

	# Definisce le linee GPIO
	GPIO.setup(22, GPIO.OUT)	# GPIO22 - Watchdog Enable
	GPIO.setup(27, GPIO.OUT)	# GPIO22 - Watchdog heartbeat
	GPIO.setup(17, GPIO.IN)		# GPIO17 - Timeout from controller

	print("Start watchdog demo!")
	print("--------------------\n")

	print("Set the watchdog enable line OFF")
	GPIO.output(22,False)

	print("Waiting 5s ...")
	time.sleep(5)

	print("Set the watchdog enable line ON")
	GPIO.output(22,True)

	print("Waiting 5s ...")
	time.sleep(5)

	print("Toggle the heartbeat line ON")
	GPIO.output(27,True)

	print("Waiting 10s ...")
	time.sleep(10)

	print("Toggle the heartbeat line OFF")
	GPIO.output(27,False)

	print("Waiting 20s ...")
	time.sleep(20)

	print("Toggle the heartbeat line ON")
	GPIO.output(27,True)

	print("--------------------------------")
	print("Stop toggling the heartbeat line")
	print("Waiting for the CM reset")
	print("--------------------------------")

	timectr=0
	while (True):
		# Legge la linea GPIO17
		GPIO17_state = GPIO.input(17)
		# Visualizza lo stato della linea
		if ( GPIO17_state == 1):
			print("Time: " + str(timectr) + "s - TIMEOUT DETECTED!!")
		else:
			print("Time: " + str(timectr) + "s - no timeout detected")
		# Attesa 1s
		time.sleep(1)
		# Aggiorna contatore tempo di attesa per visualizzazione
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


