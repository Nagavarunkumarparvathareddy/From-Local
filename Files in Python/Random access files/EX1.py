with open('myname.txt','rt') as fp:
    print(fp.tell(),fp.read(13),fp.tell())
    print(fp.tell(),fp.read(10),fp.tell())
    print(fp.tell(),fp.read(),fp.tell())
    print(fp.seek(0))
    print(fp.read(100))