"""Demonstrate how to create and use tuples."""

def main():
	# Create tuple with parentheses
	person_1 = ('Steven', 'Hester')
	# Create tuple with commas
	person_2 = 'David', 'Miller'
	# Access tuple elements via indexers
	print(f'{person_1[0]} {person_1[1]}')
	print(f'{person_2[0]} {person_2[1]}')

	# Process tuple with for loop
	for s in person_1:
		print(f'{s} ', end='')


if __name__ == '__main__':
	main()