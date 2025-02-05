import csv
with open('student.csv','r') as fp:
    file = csv.DictReader(fp)
    for ele in file:
        print(ele)