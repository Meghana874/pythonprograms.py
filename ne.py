def valid(func):
    @functools.wraps(func)
    def inner(a,b):
        if isinstance(a,str):
            a=str(a)
        if not isinstance(a,str):
            b=str(b)
        return func(a,b)
    return inner
@valid
def fun(a:str,b:str)->str:
    """This is a Docstring,This function is for  string concatenation"""
    return a+b
print(fun.__name__)
print(fun("12","13"))
print(fun.__annotations__)
print(fun.__doc__)
