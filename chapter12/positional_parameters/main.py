from greetings import greet_user

def main():
    greet_user('Coralie', 'Sylvia', 'Miller')
    greet_user('Jody', middle_name='Steiner', last_name='Kelly')
    greet_user(first_name='Jack', midle_name='Daniels', last_name='Nix')
    #greet_user(last_name='Martin', first_name='Melissa', middle_name="L'Artiste")
    

if __name__ == '__main__':
    main()