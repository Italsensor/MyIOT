#!/usr/bin/python

# ------------------------------------------------------------
# RPICM3 - Programma test utilizzo RS485
#          Modulo di ricezione e ritrasmissione (modulo slave)
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
if (len(sys.argv) <> 2):
	print("Usage:")
	print("tstserial_sl.py <baudrate>")
	sys.exit(0)

# Recupera parametri da riga di comando
script_name = sys.argv[0]
baudrate = sys.argv[1]

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

		# Inizio ciclo attesa caratteri
		print("Waiting for incoming messages...")
		
		# Ciclo principale
		while (True):
		
			# Recupero il numero di caratteri in attesa nella porta seriale
			numCtrInWaiting = ser.inWaiting()
			
			# Controllo se ci sono caratteri in attesa
			if (numCtrInWaiting > 0):
			
				rxByte = ser.read(1)
				tmpbuffer.append(rxByte)
								
				val=int(''.join(["%02X " % ord(x) for x in tmpbuffer[0]]).strip(),16)
				print("(" + str(counter) + ") RX (val):" + str(val) + "(char): " + nonPrintableChar(val))
				
				counter = counter + 1
				tmpbuffer = []
				
				# Ritrasmette indietro il carattere ricevuto (echo)
				binOutBfr.append(val)
				
				print("(" + str(counter) + ") TX (val):" + str(val) + "(char): " + nonPrintableChar(val))
				
				values = bytearray(binOutBfr)
				ser.write(values)
				binOutBfr = []
				
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
	print("Error: serial port not open!")
	print("Program exit.")
	sys.stdout.flush()
	sys.exit(1)