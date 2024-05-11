"""Demonstrate String Character Access."""

def main():
	s = "These are the times that try men's souls. " \
	"The summer soldier and the sunshine patriot will, " \
	"in this crisis, shrink from the service of their country; " \
	"but he that stands by it now, deserves the love and thanks of " \
	"man and woman. (Thomas Paine, \"The Crisis\", 23 December 1776)"
	# Access characters with array notation
	print(f'{s[0]}')
	print(f'{s[-len(s)]}')

	# Iterate over each character -- Non-Pythonic
	for i in range(len(s)):
		print(f'{s[i]}', end='')
	
	print()

	# Iterate over each character -- Pythonic
	for c in s:
		print(f'{c.upper()}', end='')

if __name__ == '__main__':
	main()

