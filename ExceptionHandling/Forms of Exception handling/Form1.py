try:
    a = int(input('Enter num1: '))
    b = int(input('Enter num2: '))
    c = a**b
    d = a/b
    print(f'{a}^{b} = {c}')
    print(f'{a}^{b} = {d}')
except ValueError:
    print('Please Enter only Int,Float values')
except ZeroDivisionError:
    print('Dont Enter 0 in num2')
    