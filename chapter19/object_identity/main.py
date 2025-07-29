"""Demonstrate object identity with the is operator."""

def main():
	o1 = object()
	o2 = o1
	o3 = object()

	print(f'o1 is o2: {o1 is o2}')
	print(f'o1 is o3: {o1 is o3}')



if __name__ == '__main__':
	main()