"""Demonstrate object instantiation and attribute access."""

from person import Person
from datetime import datetime

def main():
	p1 = Person()
	print(f'p1 = {p1} | Object Count: {Person.count}')
	p2 = Person('Rick', 'W', 'Miller', datetime(1986, 4, 2))
	print(f'p2.age = {p2.age}')
	print(f'p2 = {p2} | Object Count: {Person.count}')
	p3 = Person()
	p3.first_name = 'Hannah'
	p3.middle_name = 'J'
	p3.last_name = 'Bananna'
	p3.birthday = datetime(1994, 3, 14)
	print(f'p3 = {p3} | Object Count: {Person.count}')
	print(f'p3\'s Full Name and Age: {p3.full_name_and_age}')

	print('*' * 20)
	print(p1)


if __name__ == '__main__':
	main()
