"""Demonstrate writing files to relative paths."""

def main():
	# Bad Practice! -- Don't Do This!
	file_name = 'data\data.txt'

	try:
		with open(file_name, 'w') as f:
			f.write('Hello World!')

		with open(file_name, 'r') as f:
			print(f'{f.read()}')

	except (IOError, Exception) as e:
		print(f'Problem writing file: {e}')


if __name__ == '__main__':
	main()