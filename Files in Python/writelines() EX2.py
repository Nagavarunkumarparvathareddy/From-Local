# it does not execute as every element in x is not of 'str' type.
x= ['varun',21,'HYD','Nojob',500016,'careergap-7months']
fp = open('details.data','a')
fp.writelines(x)