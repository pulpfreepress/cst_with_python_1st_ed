"""Implements mergesort algorithm."""

import sys
import time
import random

class MergeSort():

	def __init__(self):
		self.callcount = 0


	def split(self, intlist, left, right):
		self.callcount += 1

		if __debug__: 
			print(f'split() call: {self.callcount}')
			print(intlist)
			print(f'left: {left}')
			print(f'right: {right}')
			input('Press any key to continue...')

		mid = 0
		sorted_ints = None

		if right > left:
			mid = int((right + left) / 2)
			if __debug__:
				print(f'mid: {mid}')
			self.split(intlist, left, mid)
			self.split(intlist, (mid + 1), right)
			sorted_ints = self.merge(intlist, left, (mid + 1), right)
		
		return sorted_ints


	def merge(self, intlist, left, mid, right):
		
		temp = [0] * len(intlist)
		left_end = (mid - 1)
		temp_pos = left
		num_elements = (right - left + 1)

		if __debug__:
			print('merge()...')
			print(temp)

		while (left <= left_end) and (mid <= right):
			if intlist[left] <= intlist[mid]:
				temp[temp_pos] = intlist[left]
				temp_pos += 1
				left += 1
			else:
				temp[temp_pos] = intlist[mid]
				temp_pos += 1
				mid += 1

		while left <= left_end:
			temp[temp_pos] = intlist[left]
			temp_pos += 1
			left += 1

		while mid <= right:
			temp[temp_pos] = intlist[mid]
			temp_pos += 1
			mid += 1

		if __debug__:
			print(f'num_elements = {num_elements}')

		for i in range(num_elements):
			intlist[right] = temp[right]
			right -= 1

		return intlist


def main():
	sys.setrecursionlimit(1500)
	unsorted_ints = [random.randint(0, 10000) for _ in range(20000)]
	if __debug__:
		print(unsorted_ints)
		input('Press any key to continue...')
	ms = MergeSort()
	print(f'MergeSorting {len(unsorted_ints)} randomly-generated integers. This won\'t take long...')
	t_start = time.perf_counter()
	sorted_ints = ms.split(unsorted_ints, 0, len(unsorted_ints)-1)
	t_stop = time.perf_counter()
	if __debug__:
		print(sorted_ints)
	print(f'Total sort time for {len(unsorted_ints)} integers is {t_stop - t_start:0.4f} seconds.')


if __name__ == '__main__':
	main()

				

