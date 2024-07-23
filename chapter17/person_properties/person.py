"""Contains the definition of the Person class."""

from datetime import date
from datetime import datetime
from datetime import timedelta

class Person:
	"""Defines a Person class."""
	
	# This is a class-wide attribute
	# shared by all Person objects 
	count = 0

	def __init__(self, first_name:str='John', 
			  middle_name:str='J', last_name:str='Doe',
			  birthdate:datetime=datetime.now())->None:
		"""Initializes Person object with known state."""
		self.first_name = first_name
		self.middle_name = middle_name
		self.last_name = last_name
		# Underscore warns clients not to access this attribute
		self._birthdate = birthdate
		Person.count += 1
		if __debug__:
			print(f'__init__() method called...Person object initialized!')

	@property
	def birthday(self)->datetime:
		"""Return person's birthday."""
		return self._birthdate
	
	@birthday.setter
	def birthday(self, value:datetime)->None:
		"""Set person's birthday."""
		self._birthdate = value

	@property
	def full_name(self)->str:
		"""Return person's full name."""
		return f'{self.first_name} {self.middle_name} {self.last_name}'
	
	@property
	def age(self)->int:
		"""Return person's age in years."""
		today = datetime.now().date()
		b_day = date(today.year, self._birthdate.month, self._birthdate.day)
		adjustment = (1 if today < b_day else 0)
		return (today.year - self._birthdate.year) - adjustment


	@property
	def full_name_and_age(self):
		"""Return person's full name and age."""
		return f'{self.full_name} {self.age}'


	def __str__(self)->str:
		"""Returns a string representation of the object."""
		return self.full_name

	