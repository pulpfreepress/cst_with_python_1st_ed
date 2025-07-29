"""Implements a simple echo client that connects and sends
messages to an echo server.
"""

import socket


class EchoClient():
	"""Implements the EchoClient class. """

	def __init__(self, ip:str, port:int)->None:
		"""Initialize client to connect to server on ip and port."""
		self._connect(ip, port)


	# Connect to server
	def _connect(self, ip:str, port:int)->None:
		""" Creates a socket object and connects to the server on ip address and port. """
		try:
			print(f'Connecting to server at IP Address: {ip} and Port: {port}')
			self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.client.connect((ip, port))
			print(f'Connected to IP Address: {ip} and Port: {port}')
		except Exception as e:
			print(f'Problem connecting to the server: {e}')


	# Send something to the server
	def send(self, message_string):
		""" Sends message to server and processes server response. 
		This defines the custom protocol between client and server. 
		Client sends a message and expects a response from the server.
		"""
		try:
			self.client.send(bytearray(message_string, 'utf-8'))
			
		except Exception as e:
			print(f'Problem sending message to server: {e}')


	# Process server response
	def process_server_response(self):
		""" Processes server response. Decodes raw data sent from the server."""
		try:
			raw_response = self.client.recv(2048)
			response = raw_response.decode('utf-8')
			print(f'From Server: {response}')
			
		except Exception as e:
			print(f'Problem processing server response: {e}')


	# Close connection
	def close(self):
		""" Closes the client connection.
		"""
		try:
			self.client.close()
		except Exception as e:
			print(f'Problem closing client connection: {e}')