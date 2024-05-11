"""Demonstrate string concatenation."""

def main():
	first_name = 'Rick'
	last_name = 'Miller'
	middle_initial = 'W'
	# Use Concatenation Operator '+'
	full_name = first_name + ' ' + middle_initial + ' ' + last_name
	print(full_name)

	age = 35
	# Use Formatted String a.k.a. 'F' String
	full_name_and_age = f'{first_name} {middle_initial} {last_name} {age}'
	print(full_name_and_age)

	# Long Strings with Concatenation Operator '+'
	passage_one = 'This is an example of a string that must be broken apart ' \
	'and spread across multiple lines of code.' \
	'\n\tAuthor:' + full_name + ' ' + str(age)
	print(passage_one)

	# Long Strings with F Strings
	passage_two = f'This is another long string being spread over ' \
	f'multiple lines of code.\n\tAuthor: {full_name_and_age}'
	print(passage_two)

	# Long Strings with Three Double Quotes
	passage_three = """This is a moderately long passage. The ancients knew 
the secret to long life:
	1. Eat a healthy diet,
	2. Stay active, and 
	3. Get plenty of rest.
	— Live — Love — Laugh —"""
	print(passage_three)


if __name__ == '__main__':
	main()