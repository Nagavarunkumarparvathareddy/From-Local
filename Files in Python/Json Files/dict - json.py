import json
d = {'Name':'Varun','Domain':'Python','age':21.5,'Career_status':'Unemployeed'}
with open('mydetails.json','w') as fp:
    json.dump(d,fp)
    print('Jsonfile is created')