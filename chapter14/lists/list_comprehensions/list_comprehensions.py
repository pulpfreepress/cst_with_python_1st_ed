"""Demonstrates list comprehensions."""

def main():
	# Create list of vowels
	vowels = ['A', 'E', 'I', 'O', 'U']
	# Create list of consonants
	consonants = [chr(c) for c in range(65,91) if chr(c) not in vowels]
	print(f'Consonants: {consonants}')

if __name__ == '__main__':
	main()