"""Demonstrate Abstract Base Classes."""

from hourly_employee import HourlyEmployee
from salaried_employee import SalariedEmployee
from datetime import datetime
import locale


def main():
	locale.setlocale(locale.LC_ALL, '')
	e1 = HourlyEmployee('Jack', 'Daniels', 'Nix', datetime(1987, 7,10), '0001')
	print(e1)
	e1.hours_worked = 40
	e1.hourly_rate = 165.00
	print(f'e1.pay(): {locale.currency(e1.pay(), grouping=True)}')

	e2 = SalariedEmployee('Alex', 'A', 'Remily', datetime(1993, 10, 11), '0002')
	print(e2)
	e2.yearly_salary = 252000
	print(f'e2.pay(): {locale.currency(e2.pay(), grouping=True)}')

	employees = [e1, e2]

	for e in employees:
		print(f'Employee: {e} Pay: {locale.currency(e.pay(), grouping=True)}')


if __name__ == '__main__':
	main()