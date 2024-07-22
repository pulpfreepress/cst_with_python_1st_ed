"""Demonstrate object instantiation and attribute access."""

from person import Person

def main():
	p1 = Person()
	print(f'p1 = {p1} | Object Count: {Person.count}')
	p2 = Person('Rick', 'W', 'Miller')
	print(f'p2 = {p2} | Object Count: {Person.count}')
	p3 = Person()
	p3.first_name = 'Hannah'
	p3.middle_name = 'J'
	p3.last_name = 'Bananna'
	print(f'p3 = {p3} | Object Count: {Person.count}')


if __name__ == '__main__':
	main()
