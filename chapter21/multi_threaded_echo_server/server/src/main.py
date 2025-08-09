"""Entry point for the SingleThreadedEchoServer."""


from multi_threaded_echo_server import MultiThreadedEchoServer

def main():
	try:
		m1 = MultiThreadedEchoServer('', 5000)

	except Exception as e:
		print(f'{e}')
	

if __name__ == '__main__':
	main()