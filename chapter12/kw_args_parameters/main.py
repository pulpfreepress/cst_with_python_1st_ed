from greetings import greet_user

def main():
    greet_user('Coralie', middle_name='Sylvia', last_name='Miller')
    greet_user('Jody', middle='Steiner', sir_name='Kelly')
    greet_user('Jack', middle_name='Daniels', last_name='Nix')
    greet_user('Melissa', nickname="L'Artiste", maiden_name='Martin', \
               last_name='Miller')

if __name__ == '__main__':
    main()