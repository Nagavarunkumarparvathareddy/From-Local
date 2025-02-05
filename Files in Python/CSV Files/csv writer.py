import csv

heading = ['EmpId', 'EmpName', 'EmpSal', 'EmpYOE']
records = [
    [24100, 'Varun', 3.5, 1],
    [24200, 'kumar', 10, 3.5],
    [24300, 'Parvathareddy', 25, 6],
    [24400, 'PNVK', 50, 10]
]
with open('Employeedata.csv','w') as fp:

    csvwriterobject = csv.writer(fp)
    print(csvwriterobject,type(csvwriterobject))
    csvwriterobject.writerow(heading)
    csvwriterobject.writerows(records)