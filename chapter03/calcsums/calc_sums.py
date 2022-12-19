"""Demonstrates String to Number Conversions"""

def main():
    # Read number strings from console
    num1_string = input('Enter first number: ')
    num2_string = input('Enter second number: ')
    try:
        # Convert number strings to integers
        num1 = int(num1_string)
        num2 = int(num2_string)
        # Add the numbers
        sum = num1 + num2
        # Print results using formatted string
        print(f'The sum of {num1} and {num2} = {sum}')
    except Exception as e:
        print(f'Problem converting strings to integers: {e}')


if __name__ == '__main__':
    main()