#socket will be used for easier internet checking
import socket

#internet checker
class NetChecker():
	def checkInternet(self):
		try:
	        # connect to the host -- tells us if the host is actually reachable
			socket.create_connection(("www.google.com", 80))
			socket.create_connection(("www.google.com", 443))
			return True
		except OSError:
			pass
		return False