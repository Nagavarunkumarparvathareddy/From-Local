from ExceptionCreation import *
from ExceptionHandling import *
val = input('Enter val= ')
try:
    integer(val)
except ConvertError:
    print('Enter only Interger values')
else:
    res=integer(val)
    print(res)

