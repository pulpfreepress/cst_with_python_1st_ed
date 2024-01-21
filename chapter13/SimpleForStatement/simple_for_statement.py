"""Demonstrate the use of a simple for statement."""

def main():
	try:
		input_string = input('Enter input string: ')
		separator_char = input('Enter separator char: ')
		for s in input_string:
			print(f'{s}{separator_char}', end='')

	except Exception as e:
		print(f'Problem processing input string: {e}')


if __name__ == '__main__':
	main()