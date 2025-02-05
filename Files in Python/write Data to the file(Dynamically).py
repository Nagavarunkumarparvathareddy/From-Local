fp = open('D:\\Python Pycharm\\Files in Python\\IND VS AUS TEST3.info','a')
print("Please Use STOP or stop to stop in new line to stop entering data ")
while(True):
    data = input('Enter your data: ........')
    if data == 'STOP' or data =='stop' or data == 'Stop':
        print(f'Information added to {fp.name}.Check it')
        break
    else:
        fp.writelines(data+'\n')
