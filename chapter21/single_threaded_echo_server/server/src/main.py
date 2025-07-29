"""Entry point for the SingleThreadedEchoServer."""

from single_threaded_echo_server import SingleThreadedEchoServer

def main():
	try:
		s1 = SingleThreadedEchoServer('127.0.0.1', 5000)

	except Exception as e:
		print(f'{e}')
	

if __name__ == '__main__':
	main()