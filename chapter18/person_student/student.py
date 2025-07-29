"""Define a Student class."""

from person import Person
from datetime import datetime

class Student(Person):
	"""Define Student class and associated properties and methods."""

	def __init__(self, first_name:str='John', middle_name:str='J',
			last_name:str='Doe', date_of_birth:datetime=datetime.now(),
			student_id:str='0000', major:str='none')->None:
		"""Initialize instance."""
		super().__init__(first_name, middle_name, last_name, date_of_birth)
		self.student_id=student_id
		self.major=major

	def __str__(self)->str:
		return f'{self.full_name_and_age} {self.student_id} {self.major}' 


