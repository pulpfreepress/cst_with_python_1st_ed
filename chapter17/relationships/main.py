"""Demonstrate object instantiation and attribute access."""

from person import Person
from datetime import datetime

def main():
	kyle = Person('Kyle', 'V', 'Miller', datetime(2016, 8, 12))
	rick = Person('Rick', 'W', 'Miller', datetime(1986, 4, 2))
	coralie = Person('Coralie', 'S', 'Miller', datetime(1989, 10, 6))
	print(f'{kyle} | Object Count: {Person.count}')
	print(f'{rick} | Object Count: {Person.count}')
	print(f'{coralie} | Object Count: {Person.count}')
	kyle.add_relationship(rick, 'parent')
	kyle.add_relationship(rick, 'father')
	rick.add_relationship(kyle, 'child')
	rick.add_relationship(kyle, 'son')
	kyle.add_relationship(coralie, 'parent')
	kyle.add_relationship(coralie, 'mother')
	coralie.add_relationship(kyle, 'child')
	coralie.add_relationship(kyle, 'son')
	kyle.show_relationships()
	rick.show_relationships()
	coralie.show_relationships()
	
	
	
	


if __name__ == '__main__':
	main()
