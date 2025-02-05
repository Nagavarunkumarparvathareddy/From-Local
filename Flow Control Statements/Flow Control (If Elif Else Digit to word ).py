n = int(input('Enter a number :'))
if n == 1:
    print(f'{n} is ONE')
elif n == 2:
    print(f'{n} is TWO')
elif n == 3:
    print(f'{n} is THREE')
elif n == 4:
    print(f'{n} is FOUR')
elif n == 5:
    print(f'{n} is FIVE')
elif n == 6:
    print(f'{n} is SIX')
elif n == 7:
    print(f'{n} is SEVEN')
elif n == 8:
    print(f'{n} is EIGHT')
elif n == 9:
    print(f'{n} is NINE')
elif n in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
    print('Negivite Digits')
elif n not in [-1,-2,-3,-4,-5,-6,-7,-8,-9] and n not in [1,2,3,4,5,6,7,8,9]:
    print('Number')
print('Execution Completed')