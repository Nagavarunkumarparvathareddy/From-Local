import os
fileslist = os.listdir("D:\\PYTHON FULLSTACK")
print(type(fileslist))
for i in range(1,len(fileslist)+1):
    print(i,fileslist[i-1])


