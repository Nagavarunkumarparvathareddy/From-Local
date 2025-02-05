try:
    a = int(input('Enter num1: '))
    b = int(input('Enter num2: '))
    c = a/b
except ZeroDivisionError as z:
    print(z)
except ValueError as v:
    print(v)
else:
    print(c)
finally:
    print('Program excution completed')