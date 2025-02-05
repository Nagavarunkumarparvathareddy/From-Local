import menu as m
import AddEmployee as add1
import DisplayEmployee as display1
import DisplaySingleEmployee as displayemp1
import SearchEmployee as displayemp2
import UpdateEmployee as update1
import DeleteEmployee as delete1
try:
    while(True):
        m.menu()
        ch = int(input('Enter your choice: '))
        match (ch):
            case 1:
                add1.addemployee()
            case 2:
                display1.viewemp()
            case 3:
                displayemp1.viewemp1()
            case 4:
                displayemp2.showemp()
            case 5:
                update1.update()
            case 6:
                delete1.delete()
            case 7:
                break
            case _:
                print('Please Enter valid choice')
except ValueError:
    print('Please Enter valid Number')

