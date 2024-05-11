"""Create list of consonants using ordinary means."""

def main():
	# Create list of vowels
	vowels = ['A', 'E', 'I', 'O', 'U']
	# Create empty list to hold consonants
	consonants = []
	# Step through ASCII values 65 through 90
	#   If c not a vowel add to list
	for c in range(65, 91):
		if chr(c) not in vowels:
			consonants.append(chr(c))
	
	print(f'Consonants: {consonants}')


if __name__ == '__main__':
	main()