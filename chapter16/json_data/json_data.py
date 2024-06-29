"""Demonstrate saving and reading JSON data to file."""

import json
import os

def main():
	# Create dictionary with data
	classes = {}
	classes['it-590'] = {}
	classes['it-590']['room'] = 'Ballston Center 3066'
	classes['it-590']['students'] = ['Davis', 'Lewis', 'Quinton']

	try:
		# Set up file paths
		working_dir = os.getcwd()
		data_dir = 'data'
		data_dir_path = os.path.join(working_dir, data_dir)
		filename = 'classes.json'

		# Create data directory if it does not exist
		if not os.path.exists(data_dir_path):
			os.mkdir(data_dir_path)

		# Convert data to json
		json_string = json.dumps(classes)

		# Write json to file
		with open(os.path.join(data_dir_path, filename), 'w') as f:
			f.write(json_string)

		# Press any key to continue
		input('Press any key to continue...')

		# Read the json file and convert back into dictionary
		classes = None
		json_string = None
		with open(os.path.join(data_dir_path, filename), 'r') as f:
			json_string = f.read()
			classes = json.loads(json_string)

		# Print the dictionary and JSON string
		print(f'Classes Dictionary: {classes}')
		print('*' * 20)
		print(f'JSON String: {json_string}')

	except (OSError, Exception) as e:
		print(f'Problem with file I/O: {e}')


if __name__ == '__main__':
	main()