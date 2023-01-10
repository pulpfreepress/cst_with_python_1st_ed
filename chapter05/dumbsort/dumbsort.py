"""Dumbsort Algorithm Implementation."""

class DumbSort():

	def __init__(self):
		self.int_list = None
		self.innerloop = 0
		self.outerloop = 0
		self.swaps = 0

	def run(self, integer_list):
		self.int_list = integer_list
		print(f'Sorting {self.int_list}')
		
		for i in range(12):
			self.outerloop += 1
			for j in range(1, 12):
				self.innerloop += 1
				if self.int_list[j-1] > self.int_list[j]:
					temp = self.int_list[j-1]
					self.int_list[j-1] = self.int_list[j]
					self.int_list[j] = temp
					self.swaps += 1

		for i in self.int_list:
			print(f'{i} ', end='')

		print()
		print(f'Outer loop executed {self.outerloop} times.')
		print(f'Inner loop executed {self.innerloop} times.')
		print(f'{self.swaps} swaps completed.')


def main():
	ds1 = DumbSort()
	ds1.run([1,10,7,3,9,2,4,6,5,8,0,11])
	print()
	ds2 = DumbSort()
	ds2.run([0,1,2,3,4,5,6,7,8,9,10,11])
	print()
	ds3 = DumbSort()
	ds3.run([11,10,9,8,7,6,5,4,3,2,1,0])


if __name__ == '__main__':
	main()