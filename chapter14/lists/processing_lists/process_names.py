"""Demonstrate list processing."""

from prettytable import PrettyTable

def main():
	students = list()
	students.append("Anthony Alston, Masters, IT")
	students.append("Phillip Behrns, Masters, IT")
	students.append("Lkhagvasuren Dechinlkhundev, Masters, Cybersecurity")
	students.append("Samantha King, PhD, Cybersecurity")
	students.append("Claire Madison, Masters, Cybersecurity")

	table = PrettyTable()
	table.field_names = ["Student Name", "Degree", "Major"]
	table.align = 'l'

	for student in students:
		info = student.split(',')
		table.add_row([info[0], info[1], info[2]])

	print(table)

if __name__ == '__main__':
	main()
