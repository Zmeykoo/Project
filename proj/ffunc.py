from math import inf
n='\n'
i=inf
def bigsmall(x):
	return x[0].upper() + x[1:].lower()
###################################################

def dell(num,mi,new):
	"""Редукування по рядкам(вкінці спробувати зробити один цикл)"""
	ret=0
	for j in num:
		for i in range(len(num)):
			new[ret].append(j[i]-mi[ret])
		ret+=1
def dell2(col,new1,new):
	"""Редукування по стовпцям"""
	ret=0
	for j in zip(*new):
		#print('Working??')
		for i in range(len(new)):
			new1[ret].append(j[i]-col[ret])
		ret+=1

	for x in zip(*new1):
		new1.append(x)
		del(new1[0])
	
#####Etap ?


def comp(SUMA,bs):#comparison
	"""Визначення ефективності маршрута"""
	print(comp.__doc__,'\n{} <= всі маршрути'.format(SUMA))