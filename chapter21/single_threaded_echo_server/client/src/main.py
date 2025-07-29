"""Main application for echo client. """

from echo_client import EchoClient

def main():
	try:
		client = EchoClient('127.0.0.1', 5000)

		while (input_string := input('Enter message or "q" to quit: ')).upper() not in ['Q']:
			client.send(input_string)
			client.process_server_response()
	except Exception as e:
		print(f'{e}')
	finally:	
		client.close()


if __name__ == '__main__':
	main()

