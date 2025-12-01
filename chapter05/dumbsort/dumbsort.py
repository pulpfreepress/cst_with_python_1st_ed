"""Dumb Sort Algorithm Implementation."""

import time
import random

class DumbSort():

	def run(self, int_list):
		innerloop = 0
		outerloop = 0
		swaps = 0
		
		t_start = time.perf_counter()
		for i in range(len(int_list)):
			outerloop += 1
			for j in range(1, len(int_list)):
				innerloop += 1
				if int_list[j-1] > int_list[j]:
					temp = int_list[j-1]
					int_list[j-1] = int_list[j]
					int_list[j] = temp
					swaps += 1
		t_stop = time.perf_counter()
		sort_time = t_stop - t_start

		return (int_list, outerloop, innerloop, swaps, sort_time )


def main():
	ds = DumbSort()
	list_1 = [1,10,7,3,9,2,4,6,5,8,0,11]
	print(f'Dumb sorting {len(list_1)} integers. Don\'t blink!')
	(sorted_list, outerloop, innerloop, swaps, sort_time) = ds.run(list_1)
	print(f'Outerloop: {outerloop}')
	print(f'Innerloop: {innerloop}')
	print(f'swaps: {swaps}')
	print(f'time: {sort_time:0.8f}')
	print()
	list_2 = [0,1,2,3,4,5,6,7,8,9,10,11]
	(sorted_list, outerloop, innerloop, swaps, sort_time) = ds.run(list_2)
	print(f'Outerloop: {outerloop}')
	print(f'Innerloop: {innerloop}')
	print(f'swaps: {swaps}')
	print(f'time: {sort_time:0.8f}')
	print()
	list_3 = [11,10,9,8,7,6,5,4,3,2,1,0]
	(sorted_list, outerloop, innerloop, swaps, sort_time) = ds.run(list_3)
	print(f'Outerloop: {outerloop}')
	print(f'Innerloop: {innerloop}')
	print(f'swaps: {swaps}')
	print(f'time: {sort_time:0.8f}')
	print()

	unsorted_ints = [random.randint(0, 10000) for _ in range(20000)]
	print(f'Dumb sorting {len(unsorted_ints):,} ' \
	f'randomly-generated integers. ' \
	f'This may take a while. Know any good jokes?') 
	(sorted_list, outerloop, innerloop, swaps, sort_time) = ds.run(unsorted_ints)
	print(f'Outerloop: {outerloop:,}')
	print(f'Innerloop: {innerloop:,}')
	print(f'swaps: {swaps:,}')
	print(f'time: {sort_time:0.8f}')
	

if __name__ == '__main__':
	main()