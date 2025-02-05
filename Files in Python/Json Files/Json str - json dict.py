import json
jsonstr = '{"Name":"varun","AGE":21,"Gender":"M"}'
print(jsonstr,type(jsonstr))
jsonobj = json.loads(jsonstr)
print(jsonobj,type(jsonobj))
for key,val in jsonobj.items():
    print(key,val)
