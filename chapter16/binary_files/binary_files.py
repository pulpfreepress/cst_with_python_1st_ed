"""Demonstrate binary file I/O."""

import os

def main():
	# Create some binary data
	byte_array = bytearray([0b00000000, 0b00000001, 0b00000010, 0b00000011])
	hex_bytes = b'\x0f\x05\x15\xFF'

	# Setup path variables
	working_dir = os.getcwd()
	data_dir = 'data'
	data_dir_path = os.path.join(working_dir, data_dir)
	data_file = 'binary.dat'

	try:
		if not os.path.exists(data_dir_path):
			os.makedirs(data_dir_path)

		with open(os.path.join(data_dir_path, data_file), 'wb') as f:
			bytes_written = f.write(byte_array)
			print(f'Bytes written: {bytes_written}')
			bytes_written = f.write(hex_bytes)
			print(f'Bytes written: {bytes_written}')
			print(f'File Pointer Location: {f.tell()}')

		input('Press any key to continue: ')

		with open(os.path.join(data_dir_path, data_file), 'rb') as f:
			# Opening a file for reading sets file pointer
			# to beginning of file...
			print(f'File contents: {f.read()}')
			print(f'Seek to second byte: {f.seek(1)}')
			print(f'Read second byte: {f.read(1)}')
			print(f'Read next byte: {f.read(1)}')
			print(f'File pointer location: {f.tell()}')

			print('-' * 20)
			# Reset file pointer to beginning of file
			f.seek(0)
			# Read file contents into byte array
			file_bytes = bytearray(f.read())
			# Iterate over each byte and print to console
			for b in file_bytes:
				print(f'{b:3} == {b:08b}')

	except (OSError, Exception) as e:
		print(f'Problem reading file: {e}')
	

if __name__ == '__main__':
	main()