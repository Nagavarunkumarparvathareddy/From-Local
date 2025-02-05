import pickle
def viewemp():
    try:
        with open('Employees.info','rb') as fp:
            while(True):
                employees =pickle.load(fp)
                print(employees)
    except EOFError:
        pass
