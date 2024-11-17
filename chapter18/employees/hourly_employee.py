"""Contains the definition for the HourlyEmployee class."""

from employee import Employee
from datetime import datetime

class HourlyEmployee(Employee):
	"""Implements HourlyEmployee Class."""
	def __init__(self, first_name:str='John', middle_name:str='J',
			last_name:str='Doe', date_of_birth:datetime=datetime.now(),
			employee_id:str='0000', hourly_rate:float=0.0):
		super().__init__(first_name, middle_name, last_name,
				   date_of_birth, employee_id)
		self.employee_id = employee_id
		self._hourly_rate:float = hourly_rate
		self._hours_worked:float = 0.0



	@property
	def hourly_rate(self)->float:
		return self._hourly_rate
	
	@hourly_rate.setter
	def hourly_rate(self, value)->None:
		self._hourly_rate = value

	@property
	def hours_worked(self)->float:
		return self._hours_worked
	

	@hours_worked.setter
	def hours_worked(self, value)->None:
		self._hours_worked = value;


	def pay(self)->float:
		return self.hours_worked * self.hourly_rate
	

	def __str__(self)->str:
		return f'{self.full_name_and_age} {self.employee_id}'
