"""Demonstrate building complex dictionary structure to generate valid JSON."""

import json
from datetime import datetime

def main():
	# Create dictionary following rules from table 15-2
	classes = {}
	classes['it566'] = {}
	classes['it566']['campus'] = 'Balston Center'
	classes['it566']['semester'] = 'Fall'
	classes['it566']['year'] = 2024
	classes['it566']['dates'] = {}
	classes['it566']['dates']['begin'] = datetime(2024, 8, 26).isoformat()
	classes['it566']['dates']['end'] = datetime(2024, 12, 7).isoformat()
	classes['it566']['classroom'] = '4004'
	classes['it566']['students'] = []

	s1 = {'firstName':'Kateryna', 'lastName':'Nesvit'}
	s2 = {'firstName':'Sapna', 'lastName':'Surana'}
	s3 = {'firstName':'Jose', 'lastName':'Pi'}

	classes['it566']['students'].append(s1)
	classes['it566']['students'].append(s2)
	classes['it566']['students'].append(s3)

	# Convert dictionary to JSON and write to file
	try:
		with open('classes.json', 'w') as f:
			f.write(json.dumps(classes))
	except Exception as e:
		print(f'Problem writing JSON to file: {e}')

	# Read JSON file and create new dictionary
	new_classes_dict = None
	try:
		with open('classes.json', 'r') as f:
			new_classes_dict = json.loads(f.read())
	except Exception as e:
		print(f'Problem writing JSON to file: {e}')

	if new_classes_dict != None:
		print(f'New Classes Dictionary = {new_classes_dict}')


	

if __name__ == '__main__':
	main()
