"""Demonstrate string creation."""

def main():
	# Initialize with empty string
	empty_string = ''

	# Initialize with string literal in single quotes
	first_name = 'Rick'

	# Initialize with string literal in double quotes
	last_name = "Miller"

	# Initialize with Unicode characters
	copyright = '\u00A92024'

	# Initialize with emoji
	emoji = '\N{face with tears of joy} \N{smiling face with halo}' + \
	'\N{kiss mark} \N{yawning face}'

	print(f'Empty String: {empty_string}')
	print(f'First Name: {first_name}')
	print(f'Last Name: {last_name}')
	print(f'Symbols: {copyright}')
	print(f'Emoji: {emoji}')

	for character in emoji:
		print(f'{character}  ', end='')


if __name__ == '__main__':
	main()