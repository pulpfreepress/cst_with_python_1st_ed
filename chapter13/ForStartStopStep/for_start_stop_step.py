"""Demonstrate for statement with range(start, stop, step)."""

def main():
	for i in range(5, 100, 5):
		print(f'{i} ', end='')

if __name__ == '__main__':
	main()