from greetings import create_greeting

def main():
    print(create_greeting('Coralie'))
    print(create_greeting('Kyle', ))
    print(create_greeting('Steven', 'Bishop'))
    print(create_greeting('Kateryna', '', 'Nesvit'))

    
if __name__ == '__main__':
    main()