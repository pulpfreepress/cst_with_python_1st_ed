"""Provide definition for Employee class."""

from person import Person
from payable import Payable
from abc import ABCMeta, abstractmethod
from datetime import datetime

class Employee(Person, Payable):
	"""Provide specification for an Employee entity."""
	def __init__(self, first_name:str='John', middle_name:str='J',
			last_name:str='Doe', date_of_birth:datetime=datetime.now(),
			employee_id:str='0000'):
		super().__init__(first_name, middle_name, last_name, date_of_birth)
		self.employee_id = employee_id


	@abstractmethod
	def pay(self)->float:
		pass
