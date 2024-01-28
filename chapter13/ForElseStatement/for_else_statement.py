"""Demonstrate the use of the for/else statement."""

def main():
	for i in range(5, 100, 5):
		print(f'{i} ', end='')
	else:
		print('\r\nThe for statement executed without a break.')


if __name__ == '__main__':
	main()