"""Demonstrate various ways to create and initialize lists."""

def main():
	# Create empty list
	breakfast_club = [] 
	# Then add elements
	breakfast_club.append('Rick')
	breakfast_club.append('Tri')
	breakfast_club.append('Alex')
	breakfast_club.append('Raffi')
	print(f'Breakfast Club Has {len(breakfast_club)} \
	Members: {breakfast_club}')

	# Create and initialize with a list literal
	it_566 = ['Jawaher', 'Bader', 'Matthew', 'Anthony',
		'Davis', 'Lewis', 'Joseph']
	print(f'IT-566 Class has {len(it_566)} Students: {it_566}')

	print('*' * 20)

	# Create another empty list
	list_of_lists = []
	# Then add the existing lists
	list_of_lists.append(breakfast_club)
	list_of_lists.append(it_566)
	print(f'List of Lists: {list_of_lists}')

if __name__ == '__main__':
	main()