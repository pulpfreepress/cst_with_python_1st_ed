"""Entry point for the Employee Training Application."""

import json
from argparse import ArgumentParser
from employee_training.service_layer.app_services \
	import AppServices


def main():
	"""Entry point."""
	args = configure_and_parse_commandline_arguments()

	if args.configfile:
		config = None
		with open(args.configfile, 'r') as f:
			config = json.loads(f.read())
			
		service_layer = AppServices(config)
		employees_list = service_layer.get_all_employees()
		print(employees_list)



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