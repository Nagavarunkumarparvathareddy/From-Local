import pickle
def viewemp1():
    try:
        empids = []
        with open('Employees.info', 'rb') as fp:
            try:
                while (True):
                    data = pickle.load(fp)
                    empids.append(data[0])
            except:
                pass
        eno = int(input('Enter Employee No: '))
        if eno not in empids:
            print('Employee Id is Invalid.')
        else:
            with open('Employees.info', 'rb') as fp:
                try:
                    while (True):
                        data = pickle.load(fp)
                        if data[0]== eno:
                            print(data)
                except:
                    pass
    except ValueError:
        print('Enter Employee Id number in valid format(xxxxx)..')
