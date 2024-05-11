"""Demonstrate the enumerate() function."""

from prettytable import PrettyTable

def main():
	names = ['Sarah', 'Sapna', 'Laura', 'Anita', 'Diana', 'Katerina']
	table = PrettyTable()
	table.align = 'l'
	table.field_names = ['Index', 'Name']

	for index, value in enumerate(names):
		table.add_row([index, value])

	print(table)

if __name__ == '__main__':
	main()