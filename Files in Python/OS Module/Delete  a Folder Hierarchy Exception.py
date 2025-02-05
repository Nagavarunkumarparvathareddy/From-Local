try:
    import os
    os.removedirs('asia/india/south india/')
    print('Folders Hierarchy is removed')
except FileNotFoundError:
    print('Folder with specified name is not existed')
except OSError:
    print('Folder Directory is specified fully.Please Specify folder Hirearchy Fully to delete the Folders')