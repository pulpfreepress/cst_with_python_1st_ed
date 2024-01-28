"""Demonstrate the use of the while statement."""

def main():
	input_text = ''
	while 'quit' not in input_text:
		if not (input_text == ''):
			search_string = input('Enter Search String: ')

			for s in input_text:
				if search_string in s:
					print('Found it!')
					break
			else:
				print(f'Search string \"{search_string}\" not found.')

		input_text = input('Enter Text To Be Searched: ').split()


if __name__ == '__main__':
	main()