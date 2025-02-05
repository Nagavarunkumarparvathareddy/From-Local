import pickle
def readEmployee():
    try:
        with open('EmployeeDetails.data','rb') as fp:
            Empdetails = pickle.load(fp)
            print(Empdetails)
            Empdetails = pickle.load(fp)
            print(Empdetails)
            Empdetails = pickle.load(fp)
            print(Empdetails)
            Empdetails = pickle.load(fp)
            print(Empdetails)
            Empdetails = pickle.load(fp)
            print(Empdetails)
    except FileNotFoundError:
        print('File doesnot exist')
    except EOFError:
        print('All records are read')
readEmployee()