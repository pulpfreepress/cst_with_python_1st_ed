"""Demonstrate list.sort() method."""

def main():
	letters = ['z', 'W', 'Z', 'Q', 'a', 'A', 'm']
	print(f'Original Order: {letters}')
	letters.sort()
	print(f'Default sort(): {letters}')
	letters.sort(key=str.upper)
	print(f'Specify sort key param: {letters}')

if __name__ == '__main__':
	main()