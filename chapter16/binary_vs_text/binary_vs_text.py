"""Demonstrate the difference between byte strings and text."""

import os

def main():
	byte_string = b'Coucou! Voudrais tu rejoindre moi au caf\xc3\xa9?'
	text_string = 'Coucou! Voudrais tu rejoindre moi au café?'

	working_dir = os.getcwd()
	data_dir = 'data'
	data_dir_path = os.path.join(working_dir, data_dir)
	binary_filename = 'binary_file.dat'
	text_filename = 'text_file.txt'

	try:
		if not os.path.exists(data_dir_path):
			os.makedirs(data_dir_path)

		# Write binary data
		# Binary mode takes no encoding argument
		binary_file_path = os.path.join(data_dir_path, binary_filename)
		with open(binary_file_path, 'wb') as f:
			print(f'Binary File Bytes Written: {f.write(byte_string)}')
		
		# Print file size to console
		print(f'Binary File Size: {os.path.getsize(binary_file_path)}')

		# Get text encoding to use with text mode
		encoding = input('Text Encoding (utf-8 or utf-16): ')
		if encoding not in ['utf-8', 'utf-16']:
			encoding = 'utf-8'

		# Write text data
		text_file_path = os.path.join(data_dir_path, text_filename)
		with open(text_file_path, 'w', encoding=encoding) as f:
			print(f'Text File Characters Written: {f.write(text_string)}')
			
		# Print text file size to console
		print(f'Text File Size: {os.path.getsize(text_file_path)}')

		print('*' * 50)

		# Read binary file as text
		with open(binary_file_path, 'r') as f:
			print(f'Binary File as Text: {f.read()}')

		# Read binary file as bytes
		with open(binary_file_path, 'rb') as f:
			print(f'Binary File as Bytes: {f.read()}')

		# Read text file as text
		with open(text_file_path, 'r', encoding=encoding) as f:
			print(f'Text File as Text: {f.read()}')

		# Read text file as bytes
		with open(text_file_path, 'rb') as f:
			print(f'Text File as Bytes: {f.read()}')

		
	except (OSError, Exception) as e:
		print(f'Problem writing or reading files: {e}')


if __name__ == '__main__':
	main()