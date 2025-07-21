"""Demonstrate object sorting."""

from person import Person
from datetime import datetime
from prettytable import PrettyTable


sort_by_last_name = lambda rhs: rhs.last_name


def main():
	p1 = Person('Rick', 'W', 'Miller', datetime(1989, 4, 27) )
	p2 = Person('Steven', 'H', 'Hester', datetime(1987, 12, 29))
	p3 = Person('Coralie', 'S', 'Powell', datetime(1986, 8, 9))
	p4 = Person('Melissa', 'M', 'Groth', datetime(1993, 10, 15))
	p5 = Person('Kyle', 'V', 'Miller', datetime(1988, 3, 20))
	people = [p1, p2, p3, p4, p5]
	sorted_people = sorted(people)
	sorted_people_descending = sorted(people, reverse=True)
	ad_hoc_sorted_by_last_name = sorted(people, key=sort_by_last_name)
	ad_hoc_sorted_by_last_name_descending = \
			sorted(people, key=sort_by_last_name, reverse=True)

	table = PrettyTable()
	table.field_names = ["Unsorted", "Age Ascending", "Age Descending", \
				 "Last Name Ascending", "Last Name Descending"]
	
	for i in range(5):
		table.add_row([people[i], sorted_people[i], sorted_people_descending[i], \
		ad_hoc_sorted_by_last_name[i], ad_hoc_sorted_by_last_name_descending[i]])
	
	print(table)


	# list.sort()
	print("\n\n")
	people.sort()
	for p in people:
		print(f'{p}')
	
	
if __name__ == '__main__':
	main()