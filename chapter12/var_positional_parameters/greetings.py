def greet_user(first_name, *args):
    print(f'Hello {first_name} ', end='')
    for s in args:
        print(f'{s} ', end='')
    print('!')
    

