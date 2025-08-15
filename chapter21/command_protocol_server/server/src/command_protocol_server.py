"""Implements a multi threaded command protocol server that receives and
executes commands from one or more connected client applications. Uses JSON
to exchange commands and data with the client.
"""


import socket
import os
import sys
import threading
import ifaddr
from typing import List


class CommandProtocolServer():
	"""Implements the CommandProtocolServer class."""

	def __init__(self, ip:str, port:int)->None:
		""" Initializer method takes two arguments:
			ip_address & port. 
		"""
		self.ip = ip
		self.port = port
		


	# Listen for incoming connections
	def _listen(self, ip:str, port:int)->None:
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
			self.server.listen(4)
			print(f'Listening on IP Address(es): {self._get_ipv4_addresses()}' \
		 			f' and Port: {port}')
			
		except Exception as e:
			print(f'Problem listening for incoming connection: {e}')
			self.server.close()
			sys.exit(0)


	# Accept incoming connection
	def _accept_connection(self)->None:
		"""Accepts incoming client connections. 
		Passes client socket object to separate thread for processing.
		"""
		client_count = 1
		try:
			with self.server as s:
				while True:
					print(f'Waiting for incoming client connection...')
					client, address = s.accept()
					print(f'Accepted client connection from IP Address: ' \
		   				f'{address[0]} and port {address[1]}')
					t = threading.Thread(target=self._process_client_connection, \
						  args=(client,))
					t.name = f'Client {client_count}'
					t.daemon = True
					t.start()
					client_count += 1
					
		except KeyboardInterrupt:
			print(f'\n **Server shutdown from the console.**\n')
		except Exception as e:
			print(f'Problem in _accept_connection(): {e}')
		

	# Get host IPV4 addresses
	def _get_ipv4_addresses(self)->List:
		"""Get all IPV4 addresses used on the host machine.
		Uses the ifaddr package. 
		To install: pip3 install ifaddr
		"""
		try:
			adapters = ifaddr.get_adapters()
			ips = []
			for adapter in adapters:
				for ip in adapter.ips:
					if ip.is_IPv4:
						ips.append(ip.ip)
			return ips
		except Exception as e:
			print(f'Problem in _get_all_ipv4_addresses: {e}')


	# Process client connection
	def _process_client_connection(self, client)->None:
		"""Processes client connection."""
		try:
			with client as c:
				while True:
					raw_request = c.recv(1024)
					if not raw_request:
						break
					request = raw_request.decode('utf-8')
					print(f'request from {threading.current_thread().name}: ' \
		   				f'{request}')
					c.sendall(bytearray(request, 'utf-8'))
			print(f'Client {threading.current_thread().name} ' \
		 			f'disconnected. Goodbye!')
		except Exception as e: 
			print(f'Problem in _process_client_connection(): {e}')


	def start(self)->None:
		self._listen(self.ip, self.port)
		self._accept_connection()

