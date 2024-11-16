"""Demonstrate Person-Student Inheritance."""

from person import Person
from student import Student
from datetime import datetime

def main():
	p1 = Person('Coralie', 'S', 'Miller', datetime(1988, 4, 8) )
	print(f'p1 == {p1.full_name_and_age}')

	s1 = Student('Rick', 'W', 'Miller', 
			datetime(1976, 3, 3), '20242780', 'Computer Science')
	print(f's1 == {s1}')



if __name__ == '__main__':
	main()