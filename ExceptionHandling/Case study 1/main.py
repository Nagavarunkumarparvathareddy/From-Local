from ExceptionCreation import MyError
from ExceptionHandling import div
try:
    n1 = int(input('Enter num1: '))
    n2 = int(input('Enter num2: '))
    res = div(n1,n2)
except MyError as m:
    print('Dont Enter num2 = 0')
else:
    print(res)