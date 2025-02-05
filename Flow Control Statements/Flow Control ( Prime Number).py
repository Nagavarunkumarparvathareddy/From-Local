n = int(input())
res = 'Prime'
for i in range(2,n):
    if n % i == 0:
        res= 'Non prime'
        break
if res == 'Prime':
    print(f'{n} is {res}')
else:
    print(f'{n} is {res}')