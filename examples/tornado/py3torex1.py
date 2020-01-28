# Copy the tornado folder inside the:
# /var/www/html folder
# --------------------------------------------------
# For Python2 execution: python2 py3torex1.py
# then open your browser and point to:
# http://192.168.2.228/tornado/pysocket.php
# --------------------------------------------------
# - RPi.GPIO installation
#   sudo apt-get install python-rpi.gpio
#
# - Tornado installation
#   pip install tornado
# --------------------------------------------------
# For Python3 execution: python3 py3torex1.py
# then open your browser and point to:
# http://192.168.2.228/tornado/pysocket.php
# --------------------------------------------------
# - RPi.GPIO installation
#   sudo apt-get install python3-rpi.gpio
#
# - Tornado installation
#   pip3 install tornado
# --------------------------------------------------

import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket

import RPi.GPIO as GPIO 
 
class WSHandler(tornado.websocket.WebSocketHandler):

	def check_origin(self, origin):
		return True

	def open(self):
		print("New connection was opened from " + self.request.remote_ip)
		print("Path: " + self.request.path)
		self.write_message("Welcome to my websocket!")

	def on_message(self, message):
		print("Incoming message: "+message)
		self.write_message("["+self.request.remote_ip+"] You said: " + message)
		if (message == "LOGOUT"):
			self.onCloseWrapper()
		elif (message == "QUIT"):
			self.stopTornado()
		elif (message == "LEDON"):
			GPIO.output(16, True)
		elif (message == "LEDOFF"):
			GPIO.output(16, False)

	def onCloseWrapper(self):
		self.close()
		self.on_close()
		print("LOGOUT command received...")

	def on_close(self):
		print("Connection was closed...")

	def stopTornado(self):
		tornado.ioloop.IOLoop.instance().stop()

# Function to get the IP address
def get_ip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try:
		# doesn't even have to be reachable
		s.connect(('10.255.255.255', 1))
		IP = s.getsockname()[0]
	except:
		IP = '127.0.0.1'
	finally:
		s.close()
	return IP

if __name__ == "__main__":
	
	# Set the GPIO
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(16,GPIO.OUT)
	
	# Set the tornado server
	application = tornado.web.Application([(r'/ws', WSHandler),])
	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(8888)
	
	#myIP = socket.gethostbyname(socket.gethostname())
	myIP = get_ip()
	print("Websocket Server Started at: " + myIP)
	tornado.ioloop.IOLoop.instance().start()
	
	# Exiting from application
	print("Quit application!")
