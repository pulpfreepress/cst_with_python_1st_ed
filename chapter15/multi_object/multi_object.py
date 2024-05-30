"""Demonstrate dictionaries with different types as keys and values."""

def main():
	# Numbers as keys and values
	d1 = {1:100, 2:200, 3:300}
	print(f'd1 == {d1}')

	# String keys with list and number values
	d2 = {'names': ['Judy', 'Davis', 'Lewis'], 'count':3}
	print(f'd2 == {d2}')
	
	
if __name__ == '__main__':
	main()