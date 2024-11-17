"""Contains definition for SalariedEmployee class."""

from employee import Employee
from datetime import datetime

class SalariedEmployee(Employee):
	"""Implements SalariedEmployee Class."""
	def __init__(self, first_name:str='John', middle_name:str='J',
			last_name:str='Doe', date_of_birth:datetime=datetime.now(),
			employee_id:str='0000', yearly_salary:float=0.0):
		super().__init__(first_name, middle_name, last_name,
				   date_of_birth, employee_id)
		self.employee_id = employee_id
		self._yearly_salary = yearly_salary



	@property
	def yearly_salary(self)->float:
		return self._yearly_salary
	
	@yearly_salary.setter
	def yearly_salary(self, value)->None:
		self._yearly_salary = value

	def pay(self)->float:
		return self.yearly_salary / 12 
	
	def __str__(self)->str:
		return f'{self.full_name_and_age} {self.employee_id}'
