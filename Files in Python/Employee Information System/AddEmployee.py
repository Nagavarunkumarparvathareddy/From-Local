import pickle
def addemployee():
    with open('Employees.info','rb') as fp:
        try:
            while(True):
                data = pickle.load(fp)
                empids = []
                empids.append(data[0])
        except:pass

    try:
        flag = True
        while(flag):
            with open("Employees.info",'ab') as fp:
                E_No = int(input('Enter Employee Number: '))
                if E_No in empids:
                    print('Employee Details alreday Existed...')
                    flag = False
                    break
                else:
                    E_Name = input('Enter Employee Name: ')
                    E_Desig = input('Enter Employee Designation: ')
                    E_salary = float(input('Enter Emploee salary(lakhs): '))
                    E_YOE = float(input('Enter Employee Experience: '))

                    EmpDetails = []
                    EmpDetails.append(E_No)
                    EmpDetails.append(E_Name)
                    EmpDetails.append(E_Desig)
                    EmpDetails.append(E_salary)
                    EmpDetails.append(E_YOE)
                    flag = False

            pickle.dump(EmpDetails,fp)

    except ValueError:
        print('Enter numbers not words')