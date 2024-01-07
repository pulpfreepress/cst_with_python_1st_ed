

def main():
	s1 = 'llo'
	s2 = 'hello'

	list_1 = ['hello', 'world']
	list_2 = ['llo']
	list_3 = ['hello']

	if s1 in s2:
		print(f'Yes! {s1} is in {s2}')
	else:
		print(f'No! {s1} is not in {s2}')

	if s1 in list_1:
		print(f'Yes! {s1} is in {list_1}')
	else:
		print(f'No! {s1} is not in {list_1}')

	if s2 in list_1:
		print(f'Yes! {s2} is in {list_1}')
	else:
		print(f'No! {s2} is not in {list_1}')

	if list_2 in list_1:
		print(f'Yes! {list_2} is in {list_1}')
	else:
		print(f'No! {list_2} is not in {list_1}')

	if list_3 in list_1:
		print(f'Yes! {list_3} is in {list_1}')
	else:
		print(f'No! {list_3} is not in {list_1}')



if __name__ == "__main__":
	main()