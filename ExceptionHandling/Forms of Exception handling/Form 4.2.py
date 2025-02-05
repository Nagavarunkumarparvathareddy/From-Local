try:
    a = int(input('Enter num1: '))
    b = int(input('Enter num2: '))
    c = a ** b
    d = a / b
except ValueError:
    print('Enter Int/Float Values only')
except :
    print("oop's Something went wrong")
else:
    print(f'{a}^{b} = {c}')
    print(f'{a}/{b} = {d}')
finally:
    print('          ------ X ------               ')
    print('Program Execution Completed')

