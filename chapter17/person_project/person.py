"""Contains the definition of the Person class."""

class Person:
	"""Defines a Person class."""
	
	# This is a class-wide attribute
	# shared by all Person objects 
	count = 0

	def __new__(cls, *args, **kwargs):
		"""Creates a new Person object."""
		if __debug__:
			print('__new__() method called...Person object created!')
		instance = super().__new__(cls)
		return instance


	def __init__(self, first_name:str='John', 
			  middle_name:str='J', last_name:str='Doe')->None:
		"""Initializes Person object with known state."""
		self.first_name = first_name
		self.middle_name = middle_name
		self.last_name = last_name
		Person.count += 1
		if __debug__:
			print(f'__init__() method called...Person object initialized!')


	def __str__(self)->str:
		"""Returns a string representation of the object."""
		return f'{self.first_name} {self.middle_name} {self.last_name}' 

	