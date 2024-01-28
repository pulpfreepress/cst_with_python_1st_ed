"""Demonstrate the use of an if/else statement."""

from datetime import datetime

def main():
	#today = datetime.now()
	today = datetime(2024, 1, 15)
	print(f'Today\'s Date and Time in ISO Format: {today.isoformat()}')
	print(f'Today\'s Weekday Number:  {today.isoweekday()}')
	print(f'Today\'s Weekday Name: {today.strftime("%A")}')

	if (today.strftime('%A') == 'Saturday') or (today.strftime('%A') == 'Sunday'):
		print('I love the weekends, don\'t you?')
	else:
		print(f'Oh, too bad, it\'s {today.strftime("%A")} and you must go to work!')


if __name__ == '__main__':
	main()