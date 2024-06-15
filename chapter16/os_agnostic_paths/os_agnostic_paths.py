"""Demonstrate the built-in os package."""

import os

def main():
	working_dir = os.getcwd()
	data_dir = 'data'
	data_dir_path = os.path.join(working_dir, data_dir)
	file_name = 'data.txt'

	print(f'Working Directory: {working_dir}')
	print(f'Data Directory: {data_dir_path}')

	if not os.path.exists(data_dir_path):
		os.makedirs(data_dir_path)
		
	try:
		with open(os.path.join(data_dir_path, file_name), 'w+') as f:
			input_string = ''
			while input_string != 'quit':
				input_string = input('Enter a string or "quit" to exit: ')
				if input_string != 'quit':
					f.write(f'{input_string}\n' )

			f.seek(0)
			print(f'{"*" * 20} File Contents {"*" * 20}')
			print(f'{f.read()}')

	except (OSError, Exception) as e:
		print(f'Error! {e}')


if __name__ == '__main__':
	main()