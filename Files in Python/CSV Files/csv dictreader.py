import csv
with open('data.csv','r') as fp:
    datainfile =csv.DictReader(fp)
    # <csv.DictReader object at 0x0000017EE7E4E6C0>
    print(datainfile,type(datainfile)) #  <class 'csv.DictReader'>
    print('='*50)
    for record in datainfile:
        print(record,type(record)) #<class 'dict'>
