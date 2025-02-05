from ExceptionCreation2 import NegError,NullError
from ExceptionHandling2 import multiplication
try:
    n = int(input('Enter num: '))
    multiplication(n)
except NullError:
    print("NullError: Don't Enter num = 0")
except NegError:
    print('NegError: Dont Enter num < 0')
except ValueError:
    print('ValueError: Dont Error anything other than Positive Integer Numbers')
finally:
    print('   --x--  ')
    print('Program Execution Completed')