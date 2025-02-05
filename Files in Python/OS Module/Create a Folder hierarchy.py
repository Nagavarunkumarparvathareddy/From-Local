try:
    import os
    os.makedirs('Asia\\India\\South India\\Telangana\\Hyderabad\\Ameerpet\\NareshIt Reliance Building')
    os.makedirs('\n') #OSError: [WinError 123] The filename, directory name, or volume label syntax is incorrect: '\n'
except OSError:
    print('Dont use escape sequences like \n \t as folder names')
except FileExistsError:
    print('Folder is slready exitsts at specified directory/location')