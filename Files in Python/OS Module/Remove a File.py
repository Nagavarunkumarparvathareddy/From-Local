with open('Newyear.2025','a') as fp:
    data=""
    fp.write(data)
try:
    import os
    os.remove('Newyear.202')
    print('File Removed')
except FileNotFoundError:
    print('File with that name is not found in CWD')