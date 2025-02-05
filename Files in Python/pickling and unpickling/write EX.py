# program demonstrates the data to write (list)object data into file(secondary memory)
fp = open('object.data','a')
object_data = ['value1\n','value2\n','value3\n','value4\n']
for ele in object_data:
    fp.write(ele)