"""Implements a simple echo server that receives messages
from a client application, prints it to the console, and
sends the received message back to the client.
"""

import socket
import os
import sys


class SingleThreadedEchoServer():
	"""Implements the SingleThreadedEchoServer class."""

	def __init__(self, ip:str, port:int)->None:
		""" Initializer method takes two arguments:
			ip_address & port. 
		"""
		self._listen(ip, port)
		self._accept_connection()


	# Listen for incoming connections
	def _listen(self, ip, port):
		""" Creates a server socket and starts listening on assigned 
		IP Address and Port.
		"""
		try:
			self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			if os.name == 'nt':
				self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			else:
				self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
			self.server.bind((ip, port))
			print(f'Listening on IP Address: {ip} and Port: {port} ')
			self.server.listen(4)
		except Exception as e:
			print(f'Problem listening for incoming connection: {e}')
			self.server.close()
			sys.exit(0)


	# Accept incoming connection
	def _accept_connection(self):
		""" Accepts and processes incoming client connections.
		"""
		try:
			with self.server:
				while True:
					print(f'Waiting for incoming client connection...')
					client, address = self.server.accept()
					print(f'Accepted client connection from IP Address: {address[0]} and port {address[1]}')

					with client:
						while True:
							raw_request = client.recv(1024)
							if not raw_request:
								break
							request = raw_request.decode('utf-8')
							print(f'request from client: {request}')
							client.send(bytearray(request, 'utf-8'))				
		except Exception as e:
			print(f'Problem accepting connection: {e}')