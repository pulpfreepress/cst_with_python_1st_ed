__all__ = ['calc']

add = lambda a, b : a + b
sub = lambda a, b : a - b
mul = lambda a, b : a * b
div = lambda a, b : a / b

def calc(a:float, b:float, op:str) -> float:
    result = 0
    match op:
        case '+': result = _calc(a, b, add)
        case '-': result = _calc(a, b, sub)
        case '*': result = _calc(a, b, mul)
        case '/': result = _calc(a, b, div)
    return result
    
def _calc(a:float, b:float, op:callable) -> float:
    return op(a,b)
