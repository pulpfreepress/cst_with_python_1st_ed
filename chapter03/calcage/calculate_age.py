"""Calculates users age based on their birthday."""

# Import the date and datetime classes from datetime module
from datetime import date, datetime
# Import the relativedelta function from the third-party
# dateutil.relativedelta package
from dateutil.relativedelta import relativedelta

def main():
    # Input birthday string in the format mm/dd/yyy
    date_string = input('Enter Date of Birth (mm/dd/yyyy): ')
    try:
        # Split the input string along '/' boundaries
        # This results in a list of strings
        parsed_date_list = date_string.split('/')
        # Convert month string to int
        month = int(parsed_date_list[0])
        # convert day string to int
        day = int(parsed_date_list[1])
        #convert year string to int
        year = int(parsed_date_list[2])
        # Create the birthdate date object
        birthdate = date(year=year, month=month, day=day)
        # Print birthday to console
        print(f'Your birthday is {birthdate}')
        age = relativedelta(datetime.now(), birthdate)
        print(f'You are {age.years} years old.')
        print(f'Your absolute age is: {age}')

    except Exception as e:
        print(f'Problem calculating date: {e}')


if __name__ == '__main__':
    main()