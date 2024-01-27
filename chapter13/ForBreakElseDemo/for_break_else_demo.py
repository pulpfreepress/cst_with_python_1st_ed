"""Demonstrate the use of break statement within a for loop."""

def main():
	input_text = input('Enter Text To Be Searched: ').split()
	search_string = input('Enter Search String: ')

	for s in input_text:
		if search_string in s:
			print('Found it!')
			break
	else:
		print(f'Search string \"{search_string}\" not found.')


if __name__ == '__main__':
	main()