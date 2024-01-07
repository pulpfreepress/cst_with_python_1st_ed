def create_greeting(first_name:str, middle_name:str ='Jay', last_name:str='Doe') \
    -> str:
    if isinstance(first_name, str) and isinstance(middle_name, str) and \
    isinstance(last_name, str):
        greeting = f'hello, {first_name} {middle_name} {last_name}'
        return greeting
    else:
        raise Exception('All arguments must be valid strings!')
  
