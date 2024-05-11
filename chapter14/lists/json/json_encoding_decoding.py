"""Demonstrate how to perform JSON encoding and decoding on a list."""

import json

def main():
	students = ['Davis', 'Badar', 'Matthew', 'Lewis', 'Joseph']
	print(f'students list: {students}')
	# Use json.dumps() to convert list to JSON string
	students_json = json.dumps(students)
	print(f'students_json: {students_json}')
	# Use json.loads() to create Python object from JSON string
	students_two = json.loads(students_json)
	print(f'students_two list: {students_two}')


if __name__ == '__main__':
	main()