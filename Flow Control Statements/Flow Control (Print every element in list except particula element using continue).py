n = int(input())
lst =[]
for _ in range(n):
    lst.append(int(input()))
for ele in lst:
    if ele == 29:
        continue
    print(ele, end = ' ')