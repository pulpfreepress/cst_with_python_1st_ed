"""Demonstrates object string representation."""

from person import Person
from datetime import datetime

def main():
	p1 = Person("Kyle", "Victor", "Miller", datetime(1990, 8, 10))
	print(f"repr(p1): {repr(p1)}")
	print(f" str(p1): {str(p1)}")
	print(f"f string: {p1}")
	print("--------------------------")
	print("Create p2 from repr(p1)...")
	p2 = eval(repr(p1))
	print("Print p2 in formatted string...")
	print(f'{p2}')


if __name__ == "__main__":
	main()