import pickle
def showemp():
    empids = []
    with open('Employees.info', 'rb') as fp:
        try:
            while (True):
                data = pickle.load(fp)
                empids.append(data[0])
        except:
            pass
    for ele in empids:
        print(ele)
    try:

        emp = int(input('Enter Employee id You want to look for: '))
        if emp not in empids:
            print('You selected a empid not shown above.')
        else:
            with open('Employees.info', 'rb') as fp:
                try:
                    while (True):
                        data = pickle.load(fp)
                        if data[0] == emp:
                            print(data)
                except:
                    pass
    except ValueError:
        print('Please Enter a valid Employee Id')
