"""Demonstrate the use of a simple if statement."""

from datetime import datetime

def main():
	today = datetime.now()
	print(f'Today\'s Date and Time in ISO Format: {today.isoformat()}')
	print(f'Today\'s Weekday Number:  {today.isoweekday()}')
	print(f'Today\'s Weekday Name: {today.strftime("%A")}')

	if (today.strftime('%A') == 'Saturday') or (today.strftime('%A') == 'Sunday'):
		print('I love the weekends, don\'t you?')


if __name__ == '__main__':
	main()