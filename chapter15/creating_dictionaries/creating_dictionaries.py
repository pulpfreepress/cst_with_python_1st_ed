"""Demonstrate how to create dictionaries."""

def main():
	# Print hash values of strings
	keyOne = "a"
	print(f'     keyOne.__hash__() == {keyOne.__hash__()}')
	print(f'        "a".__hash__() == {"a".__hash__()}')
	print(f'       "aa".__hash__() == {"aa".__hash__()}')
	print(f'("a" + "a").__hash__() == {("a" + "a").__hash__()}')

	# Create an empty dictionary with braces
	my_dict = {}

	# Insert a value using keyOne
	my_dict[keyOne] = "valueOne"

	# Reusing same key will overwrite stored value
	my_dict["a"] = "valueTwo"

	# Print entire dictionary
	print(f'my_dict == {my_dict}')

	# Access dictionary elements via 
	print(f'Value at my_dict[keyOne] == {my_dict[keyOne]}')
	print(f'Value at my_dict["a"] == {my_dict["a"]}')

	# Create empty dictionary with dict() constructor
	book_info = dict()
	book_info['bookTitle'] = 'Computer Scripting Techniques with Python'
	book_info['author'] = 'Rick Miller'
	book_info['isbn13'] = '978-1-932504-13-2'
	print(f'book_info == {book_info}')

	# Create dictionary with dictionary literal
	classrooms = {'bal-4004':{'instructor':'R. Miller'},
			   'bal-3066':{'instructor':'K. Nesvit'}}
	print(f'classrooms == {classrooms}')
	
if __name__ == '__main__':
	main()