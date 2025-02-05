import pickle
try:
    with open('employeedetails.data','rb') as fp:
        while(True):
            data = pickle.load(fp)
            print(data)
            print()
except FileNotFoundError:
    print('File doesnot exist')
except EOFError:
    print('All records are printed')
