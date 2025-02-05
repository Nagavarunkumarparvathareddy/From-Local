try:
    import os
    os.rmdir('"C:\\Users\\Varun\\Downloads\\chromedriver-win64"')
    print('Folder Deleted')
except FileNotFoundError:
    print('Folder Doestnot Exist in specified Directory')
except OSError:
    print('Folder is Not Empty to delete')
