try:
    n1 = float(input('Enter Number 1: '))
    n2 = float(input('Enter Number 2: '))
    ans = n1/n2
except ZeroDivisionError:
    print('Dont Enter 0 in n2 value...')
except ValueError:
    print('Enter only Integer/Float values')
else:
    print(f'{n1}/{n2}=',ans)
finally:
    print('Program Execution is Completed')