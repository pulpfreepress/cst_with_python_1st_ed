"""Demonstrate the use of the match statement."""

from datetime import datetime

def main():
	
	try:
		
		user_input = input("Enter yyyy mm dd: ").split()
		year = int(user_input[0])
		month = int(user_input[1])
		day = int(user_input[2])

		today = datetime(year, month, day)
		weekday_name = today.strftime('%A')
		print(f'Today\'s Date and Time in ISO Format: {today.isoformat()}')
		print(f'Today\'s Weekday Number:  {today.isoweekday()}')
		print(f'Today\'s Weekday Name: {weekday_name}')

		match weekday_name:
			case 'Saturday' | 'Sunday':
				print(f'It\'s {weekday_name}!  I love the weekends, don\'t you?')
			case 'Monday':
				print('It\'s manic Monday -- I wish it were Sunday!')
			case 'Tuesday':
				print(f'It\'s {weekday_name} -- I have class {weekday_name}')
			case 'Wednesday':
				print(f'I have a doctor\'s appointment on {weekday_name}!')
			case 'Thursday':
				print(f'I devote {weekday_name}s to fasting.')
			case _:
				print(f'It\'s {weekday_name}! The weekend is almost here!')

	except Exception as e:
		print(f'Problem processing date values. Please try again!: {e}')


if __name__ == '__main__':
	main()