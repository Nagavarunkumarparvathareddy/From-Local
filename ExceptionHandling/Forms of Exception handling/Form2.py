try:
    a = int(input('Enter num1: '))
    b = int(input('Enter num2: '))
    c = a ** b
    d = a / b
except (ValueError,ZeroDivisionError):
    print('Please Enter only Int,Float values')
    print('Dont Enter 0 in num2')
else:
    print(f'{a}^{b} = {c}')
    print(f'{a}/{b} = {d}')
finally:
    print('          ------ X ------               ')
    print('Program Execution Completed')

