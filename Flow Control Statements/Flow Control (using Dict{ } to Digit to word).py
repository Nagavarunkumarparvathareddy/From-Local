d = {1:'ONE',2:'TWO',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
n = int(input('Enter a Number: '))
if n == 'None':
    print('NUmber')
else:
    print(f'{n} is {d.get(n)}')