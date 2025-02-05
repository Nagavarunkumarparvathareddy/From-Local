lst = list(map(int,input().split()))
l = len(lst)
i = 0
while(i < l):
    if lst[i] < 0:
        i += 1
        continue
    else:
        print(lst[i],end= ' ')
        i += 1
