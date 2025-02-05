n = int(input())
i = 1
pro = 1
if n < 1:
    print('Invalid input')
else:
    while (i <= n):
        pro = i*pro
        i+= 1
    print(pro)