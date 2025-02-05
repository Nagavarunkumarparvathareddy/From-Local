import json
with open('mydetails.json','r') as fp:
    jsonfiledata = json.load(fp)
    print(jsonfiledata,type(jsonfiledata))
    for key,val in jsonfiledata.items():
        print(key,':',val)