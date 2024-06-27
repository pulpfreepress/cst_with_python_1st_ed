"""Demonstrate object serialization to file with Pickle package."""

import pickle
import hmac
import hashlib
import os

def main():
	try:
		# Setup path variables
		working_dir = os.getcwd()
		data_dir = 'data'
		data_dir_path = os.path.join(working_dir, data_dir)
		filename = 'classes.dat'

		if not os.path.exists(data_dir_path):
			os.mkdir(data_dir_path)

		# Some data pickle
		classes = {}
		classes['it-566'] = {}
		classes['it-566']['room'] = 'Ballston Center 4004'
		classes['it-566']['students'] = ['Wafa', 'Nawaf', 
									'Anthony', 'Dishant', 'Quinton',
									'Najoud', 'Selenge']
		
		# Pickle
		pickled_data = pickle.dumps(classes)

		# Secure to verify no tampering
		expected_digest = hmac.new(b'some_key_value', pickled_data, hashlib.sha256).hexdigest()

		# Write to file
		with open(os.path.join(data_dir_path, filename), 'wb') as f:
			f.write(pickled_data)

		# Press any key to continue
		input('Press Any Key To Continue...')


		# Read file and verify signature
		pickled_data = None
		classes = None
		with open(os.path.join(data_dir_path, filename), 'rb') as f:
			pickled_data = f.read()

		digest = hmac.new(b'some_key_value', pickled_data, hashlib.sha256).hexdigest()

		if not hmac.compare_digest(digest, expected_digest):
			print(f'Invalid signature! Data is invalid.')
			exit()
		else:
			print(f'Valid signature! Unpickling data.')
			classes = pickle.loads(pickled_data)
			print(f'{classes}')
			

		



		
	

	except (OSError, Exception) as e:
		print(f'Problem pickling data: {e}')


if __name__ == '__main__':
	main()