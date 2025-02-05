import csv

records = [
    [24200, 'Varun K', 35, 300],

]
with open('Employeedata.csv', 'a') as fp:

    csvwriterobject = csv.writer(fp)
    csvwriterobject.writerows(records)