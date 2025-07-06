"""Demonstrate object equality."""

from person import Person
from datetime import datetime


sort_by_last_name = lambda rhs: rhs.last_name


def main():
	p1 = Person('Rick', 'W', 'Miller', datetime(1989, 4, 27) )
	p2 = Person('Steven', 'H', 'Hester', datetime(1987, 12, 29))
	p3 = Person('Coralie', 'S', 'Powell', datetime(1986, 8, 9))
	p4 = Person('Melissa', 'M', 'Groth', datetime(1993, 10, 15))
	p5 = Person('Kyle', 'V', 'Miller', datetime(1988, 3, 20))
	people = [p1, p2, p3, p4, p5]
	
	print('Unsorted:')
	for p in people:
		print(f'{p.full_name_and_age}')
	
	print('\nSorted Ascending:')
	for p in sorted(people):
		print(f'{p.full_name_and_age}')

	print('\nSorted Descending (Reversed):')
	for p in sorted(people, reverse=True):
		print(f'{p.full_name_and_age}')

	print('\nAd Hoc Sort by Last Name Ascending:')
	for p in sorted(people, key=sort_by_last_name):
		print(f'{p.full_name_and_age}')

	print('\nAd Hoc Sorted by Last Name Descending (Reversed):')
	for p in sorted(people, key=sort_by_last_name, reverse=True):
		print(f'{p.full_name_and_age}')

if __name__ == '__main__':
	main()