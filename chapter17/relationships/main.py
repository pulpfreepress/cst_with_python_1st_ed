"""Demonstrate method calling."""

from person import Person
from datetime import datetime

def main():
	# Create Person Objects
	kyle = Person('Kyle', 'V', 'Miller', datetime(2016, 8, 12))
	rick = Person('Rick', 'W', 'Miller', datetime(1986, 4, 2))
	coralie = Person('Coralie', 'S', 'Miller', datetime(1989, 10, 6))
	katrina = Person('Katrina', 'M', 'Powell', datetime(1990, 12, 3))
	lois = Person('Lois', 'M', 'Miller', datetime(1966, 10, 20))
	# Print Person Info
	print(f'{kyle} | Object Count: {Person.count}')
	print(f'{rick} | Object Count: {Person.count}')
	print(f'{coralie} | Object Count: {Person.count}')
	print(f'{katrina} | Object Count: {Person.count}')
	print(f'{lois} | Object Count: {Person.count}')
	# Add Relationships
	kyle.add_relationship(rick, 'parent')
	kyle.add_relationship(rick, 'father')
	rick.add_relationship(kyle, 'child')
	rick.add_relationship(kyle, 'son')
	kyle.add_relationship(coralie, 'parent')
	kyle.add_relationship(coralie, 'mother')
	coralie.add_relationship(kyle, 'child')
	coralie.add_relationship(kyle, 'son')
	kyle.add_relationship(katrina, 'aunt')
	katrina.add_relationship(kyle, 'nephew')
	kyle.add_relationship(lois, 'grand aunt')
	lois.add_relationship(kyle, 'grand nephew')
	
	# Show Relationships
	kyle.show_relationships()
	rick.show_relationships()
	coralie.show_relationships()
	katrina.show_relationships()
	lois.show_relationships()
	
	
	
	


if __name__ == '__main__':
	main()
