"""Demonstrate saving and reading JSON data to file."""

import json
import os

def main():
	# Create dictionary with data
	classes = {}
	classes['it-590'] = {}
	classes['it-590']['room'] = 'Ballston Center 3066'
	classes['it-590']['students'] = ['Davis', 'Lewis', 'Quinton']

	print(f'Classes Dictionary:\n{classes}')
	
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
		print(f'Classes JSON:\n{json_string}')

		# Write json to file
		with open(os.path.join(data_dir_path, filename), 'w') as f:
			f.write(json_string)

		# Press any key to continue
		input('Press any key to continue...')
		print('-' * 40)

		# Read the json file and convert back into dictionary
		classes = None
		json_string = None
		with open(os.path.join(data_dir_path, filename), 'r') as f:
			print(f'Reading JSON from file...')
			json_string = f.read()
			print(f'Converting JSON string to Dictionary...')
			classes = json.loads(json_string)

		# Print the dictionary and JSON string
		print(f'JSON String:\n{json_string}')
		print(f'Classes Dictionary:\n{classes}')
	
	except (OSError, Exception) as e:
		print(f'Problem with file I/O: {e}')


if __name__ == '__main__':
	main()