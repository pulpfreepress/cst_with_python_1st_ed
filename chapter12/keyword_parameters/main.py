from greetings import greet_user

def main():
    greet_user('Coralie', middle_name='Sylvia', last_name='Miller')
    greet_user('Jody', middle_name='Steiner', last_name='Kelly')
    greet_user(first_name='Jack', middle_name='Daniels', last_name='Nix')
    greet_user(last_name='Martin', first_name='Melissa', middle_name="L'Artiste")

if __name__ == '__main__':
    main()