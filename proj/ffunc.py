from math import inf
def bigsmall(x):
	return x[0].upper() + x[1:].lower()
def line(x):
	"""Пошук найменшого рядка"""
	return min(x)
def column(new,col):
	"""Пошук найменшого стовпця"""
	print(new)
	for x in zip(*new):
		col.append(min(x))
		#print(col)
def dell(num,col,mi,new,n,i):
	"""Видалення найменошго рядка, стовпця(вкінці спробувати зробити один цикл)"""
	ret=0
	for j in num:#mi працює!!!
		for i in range(3):
			new[ret].append(j[i]-mi[ret])
		ret+=1
	#new=list()
#####
