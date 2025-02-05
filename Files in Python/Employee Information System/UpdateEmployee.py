import pickle
def update():
    empids = []
    Empalldetails = []
    with open('Employees.info', 'rb') as fp:
        try:
            while (True):
                data = pickle.load(fp)
                empids.append(data[0])
                Empalldetails.append(data)
        except:
            pass
    try:
        eno = int(input('Enter Employee Id: '))
        if eno not in empids:
            print('Employee Id is Invalid')
        else:
            try:
                E_Desig = input('Enter Employee Designation: ')
                E_salary = float(input('Enter Emploee salary(lakhs): '))
                E_YOE = float(input('Enter Employee Experience: '))
            except ValueError:
                print('Enter Valid salary or Valid YoE')
            for i in range(len(Empalldetails)):
                if Empalldetails[i][0] == eno:
                    Empalldetails[i][2] = E_Desig
                    Empalldetails[i][3] = E_salary
                    Empalldetails[i][4] = E_YOE
    except ValueError:
        print('Enter EmployeeId in valid Format(xxxxx)..')
    except:pass

    with open('Employees.info', 'wb') as fp:
        for record in Empalldetails:
            pickle.dump(record, fp)

    print("Employee details updated successfully!")
