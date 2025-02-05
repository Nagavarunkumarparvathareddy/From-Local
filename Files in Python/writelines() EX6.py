x = {1:2,3:4,5:6,7:8,9:10}
fp = open('numbers.txt','a')
fp.writelines(str(x)+'\n')