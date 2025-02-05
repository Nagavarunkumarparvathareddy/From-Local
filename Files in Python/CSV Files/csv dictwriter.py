import csv
header = ['StudId','StudName','StudGPA']
rows = [
    {'StudId':18010,'StudName':'aman','StudGPA':9.5},
    {'StudId': 18011, 'StudName': 'arjun', 'StudGPA': 8.25},
    {'StudId': 18012, 'StudName': 'Begum', 'StudGPA': 9.25},
]
with open('student.csv','w') as fp:
    csvdictwriterobject = csv.DictWriter(fp,fieldnames=header)
    print(csvdictwriterobject,type(csvdictwriterobject))
    csvdictwriterobject.writeheader()
    csvdictwriterobject.writerows(rows)
