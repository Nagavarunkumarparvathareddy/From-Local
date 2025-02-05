# Renaming a Image
try:
    with open("D:\\New folder\\Biometric\\mypic 115kb.jpg",'rb') as readimage:
       with open('varun.jpg','ab') as writeimage:
           readsource = readimage.read()
           writeimage.write(readsource)
except:pass
import os
os.rename('varun.jpg','MyImage.png')