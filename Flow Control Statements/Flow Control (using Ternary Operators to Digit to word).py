d = {1:'ONE',2:'TWO',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
n = int(input('Enter a Number: '))
result = "Number" if d.get(n) == None else d.get(n)
print(result)