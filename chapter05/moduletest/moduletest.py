"""Test Module"""

class ModuleTest():

	def __init__(self):
		pass

	def say_hi(self):
		print('Hello World!')
		print(f'My module __name__ is \'{__name__}\'')

	
def main():
	mt = ModuleTest()
	mt.say_hi()


if __name__ == '__main__':
	main()