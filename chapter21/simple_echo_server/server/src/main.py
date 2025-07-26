"""Main application for Simple Echo Server."""

from echo_server import EchoServer

def main():
	try:
		s1 = EchoServer('127.0.0.1', 5000)

	except Exception as e:
		print(f'{e}')
	

if __name__ == '__main__':
	main()