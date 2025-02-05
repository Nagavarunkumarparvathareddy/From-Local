print('='*50)
print('\t\t\t Arithmetic Operations')
print('='*50)
print('''
1. Addition
2. subtraction
3. Multiplication
4. Division
5. Floor division
6. Modular division
7. Exponentation
8. Exit
''')
print('='*50)
choice = int(input('Enter your choice : '))
match(choice):
    case 1:
        print('Addition of 2 Numbers')
        a = int(input('Enter input1 :'))
        b = int(input('Enter input2: '))
        print(f'Addition of {a} and {b} is {a+b}')
    case 2:
        print('Subtraction of 2 Numbers')
        a = int(input('Enter input1 :'))
        b = int(input('Enter input2: '))
        print(f'Subtraction of {a} and {b} is {a - b}')
    case 3:
        print('Multiplication of 2 Numbers')
        a = int(input('Enter input1 :'))
        b = int(input('Enter input2: '))
        print(f'Multiplication of {a} and {b} is {a * b}')
    case 4:
        print('Division of 2 Numbers')
        a = int(input('Enter input1 :'))
        b = int(input('Enter input2: '))
        print(f'Division of {a} and {b} is {a / b}')
    case 5:
        print('Floor division of 2 Numbers')
        a = int(input('Enter input1 :'))
        b = int(input('Enter input2: '))
        print(f'Floor division of {a} and {b} is {a // b}')
    case 6:
        print('Modulo division of 2 Numbers')
        a = int(input('Enter input1 :'))
        b = int(input('Enter input2: '))
        print(f'Modulo division  of {a} and {b} is {a % b}')
    case 7:
        print('Exponential of 2 Numbers')
        a = int(input('Enter input1 :'))
        b = int(input('Enter input2: '))
        print(f'Exponential  of {a} and {b} is {a ** b}')
    case 8:
        print('Thank you for using this program')
    case _:
        print('You Entered wrong selection.Please make your selection between b/w 1 to 8')
print('=========================Program Execution Ended==================================')



