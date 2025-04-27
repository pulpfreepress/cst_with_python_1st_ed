"""Demonstrates object string representation."""

from person import Person

def main():
	p1 = Person()
	print(repr(p1))
	print(str(p1))
	print(f'{p1}')


if __name__ == "__main__":
	main()