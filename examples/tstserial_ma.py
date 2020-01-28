#!/usr/bin/python

# ------------------------------------------------------------
# RPICM3 - Programma test utilizzo RS485
#          Modulo di trasmissione e ricezione (modulo master)
# ------------------------------------------------------------

import serial
import time
import os
import sys

counter = 0
msg = ""
rxByte = ""
tmpbuffer = []	# Buffer carattere ricevuto
binOutBfr = []	# Buffer carattere trasmesso
numCtrInWaiting = 0

# -------------------------------------------------------------
# Converte caratteri non stampabili a video nei codici
# ASCII corrispondenti e restituisce la stringa relativa
# -------------------------------------------------------------
def nonPrintableChar(code):
	asciiTbl=['NUL','SOH','STX','ETX','EOT','ENQ','ACK','BEL','BS','TAB','LF','VT','FF','CR','SO','SI','DLE','DC1','DC2','DC3','DC4','NAK','SYN','ETB','CAN','EM','SUB','ESC','FS','GS','RS','US','SPACE']
	
	if (code == 127):
		return ('DEL')
	elif (code < 33):
		return(asciiTbl[code])
	else:
		return(chr(code))

# Pulisce lo schermo
os.system("clear")

# Controllo numero argomenti da linea di comando
if (len(sys.argv) <> 5):
	print("Usage:")
	print("tstserial_ma.py <baudrate> <value1> <value2> <pause>")
	sys.exit(0)

# Recupera parametri da riga di comando
script_name = sys.argv[0]
baudrate = int(sys.argv[1])
value1 = int(sys.argv[2])
tmpctr = value1
value2 = int(sys.argv[3])
pause_tx = float(sys.argv[4])

# Configura la porta seriale
ser = serial.Serial(
	port='/dev/ttyAMA0',
	baudrate=baudrate,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)

# Controllo lo stato della porta seriale
if (ser.isOpen()):
	ser.close()

# Apre la porta seriale
try: 
	ser.open()
except Exception, e:
	print "Error: serial port open error! " + str(e)
	sys.exit(1)

# Se la porta e' effettivamente aperta prosegue
if ser.isOpen():

	try:
		
		# Svuota buffer di ricezione e di trasmissione
		ser.flushInput()
		ser.flushOutput()

		tmpctr = value1
		
		# Ciclo principale
		while (True):
		
			# Carico il valore da trasmettere
			binOutBfr.append(tmpctr)
			
			# Trasmetto una stringa di testo sulla seriale
			print("(" + str(counter) +") TX (val): " + str(tmpctr) + "(char): " + nonPrintableChar(tmpctr))
			
			values = bytearray(binOutBfr)
			ser.write(values)
			binOutBfr = []
			
			# Determino la modalita' scelta singolo o sweep
			if (value1 == value2):
				# Valori uguali
				tmpctr = value1
			else:
				# Eseguo lo sweep dei valori
				tmpctr = tmpctr + 1
				if (tmpctr > value2):
					tmpctr = value1

			# Attesa per risposta
			if (pause_tx <> 0):
				time.sleep(pause_tx)
				
			# Legge tutti i caratteri ricevuti
			tmpbuffer = []
			numCtrInWaiting = ser.inWaiting()
			while (numCtrInWaiting > 0):
				rxByte = ser.read(1)
				tmpbuffer.append(rxByte)
				val=int(''.join(["%02X " % ord(x) for x in tmpbuffer[0]]).strip(),16)
				print("(" + str(counter) +") RX (val): " + str(val) + "(char): " + nonPrintableChar(val))
				tmpbuffer = []
				numCtrInWaiting = ser.inWaiting()
		
			# Aggiorno contatore caratteri trasmessi
			counter = counter + 1

		# Fine attivita' chiudo la porta seriale
		ser.close()
		
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

else:
	print "Error: serial port not open!"
	print("Program exit.")
	sys.stdout.flush()
	sys.exit(1)
