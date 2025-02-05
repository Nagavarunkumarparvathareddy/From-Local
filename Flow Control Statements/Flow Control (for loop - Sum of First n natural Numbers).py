n = int(input())
sum = 0
square = 0
cube = 0
product = 1
for i in range(1,n+1):
    sum += i
    square += i**2
    cube += i**3
    product *= i
print(f'sum of first {n} :',sum)
print(f'Squares of first {n} :',square)
print(f'Cubes of first {n} :',cube)
print(f'Product of first {n} :',product)