# It cannot be executed because x is object of <class,list>
# any thing other str type causes type error
x= ['varun',21,'HYD','Nojob',500016,'careergap-7months']
fp = open('details.data','a')
fp.write(x)