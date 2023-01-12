"""Dumbsort Algorithm Implementation."""

import time
import random

class DumbSort():

	def run(self, int_list):
		innerloop = 0
		outerloop = 0
		swaps = 0
		
		for i in range(len(int_list)):
			outerloop += 1
			for j in range(1, len(int_list)):
				innerloop += 1
				if int_list[j-1] > int_list[j]:
					temp = int_list[j-1]
					int_list[j-1] = int_list[j]
					int_list[j] = temp
					swaps += 1
		
		if __debug__:
			print()
			print(f'Outer loop executed {outerloop} times.')
			print(f'Inner loop executed {innerloop} times.')
			print(f'{swaps} swaps completed.')

		return int_list


def main():
	ds = DumbSort()
	list_1 = [1,10,7,3,9,2,4,6,5,8,0,11]
	print(f'DumbSorting {len(list_1)} integers. Don\'t blink!')
	t_start = time.perf_counter()
	ds.run(list_1)
	t_stop = time.perf_counter()
	print(f'Total sort time for {len(list_1)} integers is {t_stop - t_start:0.4f} seconds.')
	print()
	list_2 = [0,1,2,3,4,5,6,7,8,9,10,11]
	t_start = time.perf_counter()
	ds.run(list_2)
	t_stop = time.perf_counter()
	print(f'Total sort time for {len(list_2)} integers is {t_stop - t_start:0.4f} seconds.')
	print()
	list_3 = [11,10,9,8,7,6,5,4,3,2,1,0]
	t_start = time.perf_counter()
	ds.run(list_3)
	t_stop = time.perf_counter()
	print(f'Total sort time for {len(list_3)} integers is {t_stop - t_start:0.4f} seconds.')
	print()
	unsorted_ints = [random.randint(0, 10000) for _ in range(20000)]
	print(f'DumbSorting {len(unsorted_ints)} randomly-generated integers. \
	This may take a while. Know any good jokes?')
	t_start = time.perf_counter()
	ds.run(unsorted_ints)
	t_stop = time.perf_counter()
	print(f'Total sort time for {len(unsorted_ints)} integers is {t_stop - t_start:0.4f} seconds.')

	
if __name__ == '__main__':
	main()