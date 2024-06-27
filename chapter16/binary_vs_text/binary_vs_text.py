"""Demonstrate the difference between byte strings and text."""

import os

def main():
	byte_string = b'Hello World!'
	text_string = 'Hello World!'


	working_dir = os.getcwd()
	data_dir = 'data'
	data_dir_path = os.path.join(working_dir, data_dir)
	binary_filename = 'binary_file.dat'
	text_filename = 'text_file.txt'

	try:
		if not os.path.exists(data_dir_path):
			os.makedirs(data_dir_path)

		# Write binary data
		binary_file_path = os.path.join(data_dir_path, binary_filename)
		with open(binary_file_path, 'wb') as f:
			print(f'Binary File Bytes Written: {f.write(byte_string)}')
		
		# Print file size to console
		print(f'Binary File Size: {os.path.getsize(binary_file_path)}')

		# Get text encoding to use
		encoding = input('Text Encoding (utf-8 or utf-16): ')

		if encoding not in ['utf-8', 'utf-16']:
			encoding = 'utf-8'

		# Write text data
		text_file_path = os.path.join(data_dir_path, text_filename)
		with open(text_file_path, 'w', encoding=encoding) as f:
			print(f'Text File Characters Written: {f.write(text_string)}')
			
		# Print text file size to console
		print(f'Text File Size: {os.path.getsize(text_file_path)}')

		# Read text file as bytes and print to console
		with open(text_file_path, 'rb') as f:
			print(f'Text File Bytes: {f.read()}')

	except (OSError, Exception) as e:
		print(f'Problem writing files: {e}')


if __name__ == '__main__':
	main()