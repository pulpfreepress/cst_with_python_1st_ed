"""Demonstrate Type Checking with isinstance() Function."""
from employee import Employee
from hourly_employee import HourlyEmployee
from salaried_employee import SalariedEmployee
from datetime import datetime
import locale


def main():
	"""Entry point. """
	e1 = HourlyEmployee('Jack', 'Daniels', 'Nix', datetime(1987, 7,10), '0001')
	e1.hours_worked = 40
	e1.hourly_rate = 165.00
	
	e2 = SalariedEmployee('Alex', 'A', 'Remily', datetime(1993, 10, 11), '0002')
	e2.yearly_salary = 252000

	
	employees = [e1, e2]

	for e in employees:
		print_employee_info(e)

	
def print_employee_info(employee:Employee):
	"""Print employee information.
	Expects object passed as employee argument to 
	be of type Employee.
	"""
	if not isinstance(employee, Employee):
		raise TypeError('Invalid type for employee argument!')
	
	locale.setlocale(locale.LC_ALL, '')

	print(f'Employee: {employee}\nPay: \
	   {locale.currency(employee.pay(), grouping=True)}\n\n')



if __name__ == '__main__':
	main()