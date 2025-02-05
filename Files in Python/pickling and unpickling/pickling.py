import pickle
def Employeedetails():
    with open('EmployeeDetails.data','ab') as fp:
        try:
            while(True):
                Eno = int(input('Enter Employee No: '))
                Ename = input('Enter Employee Name: ')
                Exp = float(input('Enter Years of experience: '))
                Etech = input('Enter Employee tech stack: ')
                Esal = float(input('Enter Employee salary in Lakhs: '))

                object = []
                object.append(Eno)
                object.append(Ename)
                object.append(Exp)
                object.append(Etech)
                object.append(Esal)

                pickle.dump(object,fp)
                print('Employee details are added..')
                cond = input('Do you want to add another employee record(yes/no): ').lower()
                if cond != 'yes':
                    break
        except ValueError:
            print('Enter only Int values')

Employeedetails()

