import os
fileslist = os.listdir("D:\\PYTHON FULLSTACK")
pdf = []
for ele in fileslist:
    if ele.endswith('pdf'):
        pdf.append(ele)
for ele in pdf:
    print(ele)