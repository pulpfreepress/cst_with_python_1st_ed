"""Demonstrate simple string searching."""

def main():
	s = 'Now friendship may be thus defined: a complete accord on all subjects \n' \
'human and divine, joined with mutual goodwill and affection. And with \n' \
'the exception of wisdom, I am inclined to think nothing better than this \n' \
'has been given to man by the immortal gods. There are people who give \n' \
'the palm to riches or to good health, or to power and office, many even \n' \
'to sensual pleasures. This last is the ideal of brute beasts; and of the \n' \
'others we may say that they are frail and uncertain, and depend less on \n' \
'our own prudence than on the caprice of fortune. Then there are those \n' \
'who find the "chief good" in virtue. Well, that is a noble doctrine. But \n' \
'the very virtue they talk of is the parent and preserver of friendship, \n' \
'and without it friendship cannot possibly exist. "Cicero" \n' 
	
	print(s)
	
	# Is substring in string
	if 'friendship' in s:
		print('Yes, the word \"friendship\" is in the passage.')
	else:
		print('The word \"friendship\" not found.')

	# At what index position does substring begin
	# Start searching from 0 index (start of string)
	print(f'The word \"friendship\" begins at index {s.find("friendship")}')

	# At what index position does substring begin
	# Start searching at index position n
	print(f'The next occurence of \"friendship\" begins at index {s.find("friendship",5)}')


if __name__ == '__main__':
	main()