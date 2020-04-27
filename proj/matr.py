#Матриця на 3 міста Львів, Київ, Черкаси
from math import inf
import ffunc
i=inf;n='\n'

num=[[i,1,4],[8,i,2],[4,9,i]]
new=[[],[],[]]

mi=list(map(ffunc.line,num))#min line


ffunc.dell(num,mi,new)
col=[min(x) for x in zip(*new)]#min column

SUMA=sum(mi)+sum(col)

print(n,num[0],n,num[1],n,num[2])	
print(n,'Min numbers of line(рядок):',mi)
print(n,'after reducing',n,new[0],n,new[1],n,new[2])
print(n,'Min num of column(стовпець)',col,n,'Сума констант редукції:',SUMA)