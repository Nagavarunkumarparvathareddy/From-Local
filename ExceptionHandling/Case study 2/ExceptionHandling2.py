from ExceptionCreation2 import *
def multiplication(n):
    if n == 0:
        raise NullError
    elif n < 0:
        raise NegError
    else:
        for i in range(1,11):
            print(f'{n} x {i} = {n*i}')