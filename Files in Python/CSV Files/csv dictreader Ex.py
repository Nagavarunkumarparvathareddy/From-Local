import csv
with open('data.csv','r') as fp:
    datainfile =csv.DictReader(fp)
    for record in datainfile:
        for key,val in record.items():
            print(key,val)
        print('-'*25)