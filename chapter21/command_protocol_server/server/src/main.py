"""Entry point for the SingleThreadedEchoServer."""


from command_protocol_server import CommandProtocolServer
from argparse import ArgumentParser

def main():
	try:
		args = configure_and_parse_commandline_arguments()
		
		if (args.ipaddress != None) and args.port:
			print(f'IP: {args.ipaddress} Port:{args.port}')
			ip_address = args.ipaddress
			port = args.port

		server = CommandProtocolServer(ip=ip_address, port=port)
		server.start()

	except Exception as e:
		print(f'{e}')
	


def configure_and_parse_commandline_arguments():
	"""Configure and parse command-line arguments."""
	parser = ArgumentParser(
	prog='main.py',
	description='Start Command Protocol Server.',
	epilog='POC: Rick Miller | rick@pulpfreepress.com')
	
	parser.add_argument('-ip','--ipaddress', 
					default='',
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