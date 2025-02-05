try:
    import os
    os.mkdir('D:\\PYTHON FULLSTACK\\1.Python KVR\\Notes Python KVR\\Operating_systems\\OaS\\varun')
    print('File created please check it')
except FileExistsError:
    print('Folder is already exists at that location')
except FileNotFoundError:
    print('Folder is Not founde to create a another folder int it')