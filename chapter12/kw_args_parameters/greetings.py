def greet_user(first_name, **kwargs):
    print(f'{first_name}', end='')
    for key, value in kwargs.items():
        print(f', {key}={value}', end='')
    print('!')
    

