"""Demonstrate simple file operations."""


def main():
	filename = 'data.txt'
	input_text = None

	try:
		while True:
			# Get user's input
			input_text = input('Enter some text: ')

			# Exit program if user enters 'quit'
			if input_text == 'quit':
				exit()

			# Write user's input to a file
			with open(filename, 'w') as f:
				f.write(input_text)
				

			input('Press any key to continue: ')

			# read text from a file 
			with open(filename, 'r') as f:
				print(f'You Entered: {f.read()}')

	except (OSError, Exception) as e:
		print(f'Problem writing file: {e}')


if __name__ == '__main__':
	main()