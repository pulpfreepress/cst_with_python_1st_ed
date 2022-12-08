message = 'Hello World!'
print(message.lower())
print(message.capitalize())
print(message.upper())
print(message.center(40, '-'))
print('*' * 60)
name = input('What\'s your name? ')
message = message.removesuffix('World!')
print(message + ' ' + name + '!')

