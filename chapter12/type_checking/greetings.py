import typing

def greet_user(first_name:str, middle_name:str ='Jay', last_name:str='Doe') \
    -> None:
    if isinstance(first_name, str) and isinstance(middle_name, str) and \
        isinstance(last_name, str):
        print(f'hello, {first_name} {middle_name} {last_name}')
    else:
        raise Exception('Arguments must be strings!')
    
  
