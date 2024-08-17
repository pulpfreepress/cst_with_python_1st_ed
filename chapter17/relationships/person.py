"""Contains the definition of the Person class."""

from datetime import date
from datetime import datetime

class Person:
	"""Defines a Person class."""
	
	# This is a class-wide attribute
	# shared by all Person objects
	# Define and initialize these first
	count = 0

	# Define the __init__() method next
	def __init__(self, first_name:str='John', 
			  middle_name:str='J', last_name:str='Doe',
			  date_of_birth:datetime=datetime.now())->None:
		"""Initializes Person object with known state."""
		self.first_name = first_name
		self.middle_name = middle_name
		self.last_name = last_name
		# Underscore warns clients not to access this attribute
		self._dob = date_of_birth
		self._relationships = {}
		Person.count += 1
		

	# Define properties next
	# Group property definition with 
	# corresponding setters and deleters (if any)
	@property
	def birthday(self)->datetime:
		"""Return person's birthday."""
		return self._dob
	

	@birthday.setter
	def birthday(self, value:datetime)->None:
		"""Set person's birthday."""
		self._dob = value


	@property
	def full_name(self)->str:
		"""Return person's full name."""
		return f'{self.first_name} {self.middle_name} {self.last_name}'
	

	@property
	def age(self)->int:
		"""Return person's age in years."""
		today = datetime.now().date()
		b_day = date(today.year, self._dob.month, self._dob.day)
		adjustment = (1 if today < b_day else 0)
		return (today.year - self._dob.year) - adjustment


	@property
	def full_name_and_age(self):
		"""Return person's full name and age."""
		return f'{self.full_name} {self.age}'


	def __str__(self)->str:
		"""Returns a string representation of the object."""
		return self.full_name_and_age
	
	
	def add_relationship(self, p, relationship:str)->None:
		if relationship not in self._relationships:
			self._relationships[relationship] = []

		match(relationship):
			case 'parent' | 'father' | 'mother' \
				| 'sibling' | 'brother' | 'sister' \
				| 'child' | 'daughter' | 'son' \
				| 'aunt' | 'uncle' | 'niece' | 'nephew':
				if isinstance(p, Person):
					if p not in self._relationships[relationship]:
						self._relationships[relationship].append(p)
			case _:
				self._relationships[relationship].append(p)


	def show_relationships(self):
		for key in self._relationships:
			for entry in self._relationships[key]:
				print(f'{self.full_name} --> {key} : {entry}')
	
	