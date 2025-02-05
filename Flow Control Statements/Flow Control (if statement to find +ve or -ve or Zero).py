n = float(input('Enter a number: '))
if not isinstance(n,float):
    print('Go and learn Numbers')
if n > 0:
    print(f'{n} is *ve')
if n < 0:
    print(f'{n} is -Ve')
if n == 0:
    print(f'{n} is zero')
print('==== Program execution completed ====')