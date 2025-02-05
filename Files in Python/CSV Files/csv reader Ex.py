import csv
fp = open('Data.csv', 'r')
datainfile = csv.reader(fp)
for ele in datainfile:
    for val in ele:
        print(val,end='\t')
    print()
fp.close()