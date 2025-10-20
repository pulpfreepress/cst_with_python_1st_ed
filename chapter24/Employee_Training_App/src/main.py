"""Entry point for the Employee Training Application."""

import json
from argparse import ArgumentParser
from employee_training.persistence_layer.mysql_persistence_wrapper \
	import MySQLPersistenceWrapper


def main():
	"""Entry point."""
	args = configure_and_parse_commandline_arguments()

	if args.configfile:
		config = None
		with open(args.configfile, 'r') as f:
			config = json.loads(f.read())
			
		db = MySQLPersistenceWrapper(config)
		employees_list = db.select_all_employees()
		for employee in employees_list:
			print(f'{employee}')

		print('*' * 40)
		employees_list = db.select_all_employees_with_training()
		for employee in employees_list:
			print(f'{employee}')

		print('*' * 40)
		employees_list = db.select_all_employees()
		for employee in employees_list:
			print(f'{employee[1]} {employee[3]}')
			training_list = db.select_all_training_for_employee_id(employee[0])
			for training in training_list:
				training_string = f'\t{training[0]} {training[1]} {training[2]} ' \
					f'{training[3]} {training[4]}'
				print(training_string)



def configure_and_parse_commandline_arguments():
	"""Configure and parse command-line arguments."""
	parser = ArgumentParser(
	prog='main.py',
	description='Start the Employee Training App with a configuration file.',
	epilog='POC: Rick Miller | rick@pulpfreepress.com')

	parser.add_argument('-c','--configfile',
					help="Configuration file to load.",
					required=True)
	args = parser.parse_args()
	return args



if __name__ == "__main__":
	main()