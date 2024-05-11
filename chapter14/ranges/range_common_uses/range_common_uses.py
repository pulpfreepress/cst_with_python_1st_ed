"""Demonstrate common uses of ranges."""

def main():
	# To loop n number of times
	for i in range(10):
		print(f'{i}, ', end='')

	print()

	# Specify start, stop, and step
	for i in range(2, 100, 10):
		print(f'{i}, ', end='')

	print()

	# Assign range to variable
	range_one = range(10)
	range_two = range(10, 21)
	print(f'{range_one}')
	print(f'{range_two}')

	# Create list from range
	num_list = list(range_one)
	print(f'{num_list}')

	# Extend list with range
	num_list.extend(range_two)
	print(f'{num_list}')

	# Check for membership
	print(f'5 in range_one: {5 in range_one}')
	print(f'5 in range_two: {5 in range_two}')


if __name__ == '__main__':
	main()