from math import inf
def bigsmall(x):
	return x[0].upper() + x[1:].lower()
def line(x):
	"""Пошук найменшого рядка"""
	return min(x)

def dell(num,mi,new):
	"""Видалення найменошго рядка, стовпця(вкінці спробувати зробити один цикл)"""
	ret=0
	for j in num:
		for i in range(3):
			new[ret].append(j[i]-mi[ret])
		ret+=1
	#new=list()
#####
