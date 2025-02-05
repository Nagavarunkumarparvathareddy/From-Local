import csv
fp = open('Data.csv', 'r')
datainfile = csv.reader(fp)
# datainfile = <_csv.reader object at 0x000001EFB3C69840>
print(datainfile,type(datainfile)) # <class '_csv.reader'>
print('='*50)
for ele in datainfile:
    print(ele,type(ele)) # <class 'list'>