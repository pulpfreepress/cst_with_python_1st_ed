"""Demonstrate dictionary view objects."""

def main():
	# Create and initialize dictionary
	animals = {}
	animals['zebra'] = 'Horse-like animal with black and white stripes.'
	animals['rooster'] = 'Male chicken. Very annoying in the morning.'
	animals['dog'] = 'Man\'s best friend.'
	animals['cat'] = 'Internet star!'

	# Extract view object
	animal_items = animals.items()

	# Iterate over view object's key/value pairs
	for key, value in animal_items:
		print(f'{key} : {value}')

	# Add another item
	animals['pony'] = 'Every little girl\'s dream.'

	print('*' * 60)

	# Iterate over view object's sorted key/value pairs
	for key, value in sorted(animal_items):
		print(f'{key} : {value}')


if __name__ == '__main__':
	main()