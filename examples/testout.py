#!/usr/bin/python

# --------------------------------------------
# RPICM3 - Programma esempio pilotaggio uscite
# --------------------------------------------

import RPi.GPIO as GPIO
import time

# Disattiva warnings GPIO
GPIO.setwarnings(False)

# Imposta modalita' utilizzo GPIO
GPIO.setmode(GPIO.BCM)

# Definisce le linee GPIO come uscite
GPIO.setup(12, GPIO.OUT) # O12
GPIO.setup(13, GPIO.OUT) # O11
GPIO.setup(20, GPIO.OUT) # O21
GPIO.setup(26, GPIO.OUT) # O13
GPIO.setup(35, GPIO.OUT) # O24
GPIO.setup(36, GPIO.OUT) # O23
GPIO.setup(37, GPIO.OUT) # O22
GPIO.setup(38, GPIO.OUT) # O14

GPIO.setup(16, GPIO.OUT) # DL3
GPIO.setup(34, GPIO.OUT) # DL4

# Definisco le linee di ENABLE
# per i due gruppi di GPIO
GPIO.setup(21, GPIO.OUT)	# Enable driver 1 (O11,O12,O13,O14)
GPIO.setup(11, GPIO.OUT)  # Enable driver 2 (O21,O22,O23,O24)

# Attiva i driver esterni
GPIO.output(21, True)
GPIO.output(11, True)

# Ciclo attivazione singola uscita
counter = 0
MAXCOUNT = 5
while (True):

	print("ciclo: " + str(counter))

	GPIO.output(26, False)
	GPIO.output(36, True)
	time.sleep(0.5)
	GPIO.output(36, False)
	GPIO.output(20, True)
	time.sleep(0.5)
	GPIO.output(20, False)
	GPIO.output(37, True)
	time.sleep(0.5)
	GPIO.output(37, False)
	GPIO.output(35, True)
	time.sleep(0.5)
	GPIO.output(35, False)
	GPIO.output(38, True)
	time.sleep(0.5)
	GPIO.output(38, False)
	GPIO.output(13, True)
	time.sleep(0.5)
	GPIO.output(13, False)
	GPIO.output(12, True)
	time.sleep(0.5)
	GPIO.output(12, False)
	GPIO.output(26, True)
	time.sleep(0.5)
	
	GPIO.output(26, False)
	GPIO.output(12, True)
	time.sleep(0.5)
	GPIO.output(12, False)
	GPIO.output(13, True)
	time.sleep(0.5)
	GPIO.output(13, False)
	GPIO.output(38, True)
	time.sleep(0.5)
	GPIO.output(38, False)
	GPIO.output(35, True)
	time.sleep(0.5)
	GPIO.output(35, False)
	GPIO.output(37, True)
	time.sleep(0.5)
	GPIO.output(37, False)
	GPIO.output(20, True)
	time.sleep(0.5)
	GPIO.output(20, False)
	GPIO.output(36, True)
	time.sleep(0.5)
	
	counter+=1
	if (counter == MAXCOUNT):
		break

print("Attiva tutte le uscite")

# Attivo tutti i led
GPIO.output(36, True)
GPIO.output(20, True)
GPIO.output(37, True)
GPIO.output(35, True)
GPIO.output(38, True)
GPIO.output(13, True)
GPIO.output(12, True)
GPIO.output(26, True)

print("Spengo secondo gruppo uscite (3 state)")

# Spengo tutto il secondo gruppo
# disattivando il secondo driver
time.sleep(2)
GPIO.output(21, True)
GPIO.output(11, False)

print("Spengo primo gruppo uscite (3 state)")

# Spengo tutto il primo gruppo
# disattivando il primo driver
time.sleep(2)
GPIO.output(21, False)
GPIO.output(11, True)
time.sleep(2)

print("Spengo tutte le uscite (3 state)")

# Spengo tutti i led disattivando
# entrambi i driver
GPIO.output(21, False)
GPIO.output(11, False)

print("Lampeggio led DL3 e DL4")

counter = 0
MAXCOUNT = 5
while (True):
	
	GPIO.output(16, True)
	GPIO.output(34, False)
	time.sleep(1)
	GPIO.output(16, False)
	GPIO.output(34, True)
	time.sleep(1)
	
	counter+=1
	if (counter == MAXCOUNT):
		GPIO.output(16, False)
		GPIO.output(34, False)
		break

print("Fine test uscite")

# Attiva warnings GPIO
GPIO.setwarnings(True)
