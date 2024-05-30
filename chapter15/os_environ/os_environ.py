"""Demonstrates the use of the os.environ dictionary."""

import os
from prettytable import PrettyTable

def main():
	for key, value in os.environ.items():
		print(f'{key} : {value}')


if __name__ == '__main__':
	main()