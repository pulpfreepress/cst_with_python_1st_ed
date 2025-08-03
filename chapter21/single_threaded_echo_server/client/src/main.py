"""Main application for echo client. """

from echo_client import EchoClient
from argparse import ArgumentParser

def main():
	"""Entry point."""
	client = None
	try:
		args = configure_and_parse_commandline_arguments()
		
		if args.ipaddress and args.port:
			print(f'IP: {args.ipaddress} Port:{args.port}')
			ip_address = args.ipaddress
			port = args.port

			client = EchoClient(ip=ip_address, port=port)

			while (input_string := \
		  		input('Enter message or "q" to quit: ')).upper() not in ['Q']:
				client.send(input_string)
				client.process_server_response()
	except Exception as e:
		print(f'{e}')
	finally:	
		if client:
			client.close()


def configure_and_parse_commandline_arguments():
	"""Configure and parse command-line arguments."""
	parser = ArgumentParser(
	prog='main.py',
	description='Start Echo Client Application.',
	epilog='POC: Rick Miller | rick@pulpfreepress.com')
	
	parser.add_argument('-ip','--ipaddress', 
					default='127.0.0.1',
					type=str,
					help="Server's IP address.",  
					required=False)
	
	parser.add_argument('-p','--port',
					default=5000, 
					type=int,
					help="Port to connect to.",  
					required=False)
	
	args = parser.parse_args()
	return args


if __name__ == '__main__':
	main()

