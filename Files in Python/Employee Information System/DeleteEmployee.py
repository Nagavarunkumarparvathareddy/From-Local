import pickle
def delete():
    with open('Employees.info','rb') as fp:
        try:
            empids = []
            alldetails = []
            while(True):
                data = pickle.load(fp)
                empids.append(data[0])
                alldetails.append(data)
        except:pass
    try:
        eid = int(input('Enter Employee Id: '))
        if eid not in empids:
            print('Employee Id is not available in database')
        else:
            try:
                for i in range(len(empids)):
                    if empids[i] == eid:
                        alldetails.pop(i)
            except:pass
    except:
        print('Enter valid Employee Id')

    with open('Employees.info','wb') as fp:
        for record in alldetails:
            pickle.dump(record,fp)
    print('Employee record is Deleted sucessfully ....')
