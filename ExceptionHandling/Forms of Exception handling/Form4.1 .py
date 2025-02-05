try:
    a = int(input('Enter num1: '))
    b = int(input('Enter num2: '))
    c = a ** b
    d = a / b
# Default except block
except :
    print("oop's Something went wrong")
#except ZeroDivisionError:
#   print('division by zero')
#SyntaxError: default 'except:' must be last
else:
    print(f'{a}^{b} = {c}')
    print(f'{a}/{b} = {d}')
finally:
    print('          ------ X ------               ')
    print('Program Execution Completed')

