

def decorator_sssss(func_to_decorate):
    def wrapper():
        print('22222')
        one = func_to_decorate()
        print('3333333')
        return one
    return wrapper

@decorator_sssss
def one():
    print('11111111')
    return '121212'


@decorator_sssss
def two():
    print('11111111')
    return '121212'

one_var = one()
print(one_var)