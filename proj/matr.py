#Матриця на 3 міста Львів, Київ, Черкаси
from math import inf
import ffunc
i=inf;n='\n'

num=[[i,1,4],[8,i,2],[4,9,i]]
mi=list(map(ffunc.line,num))#min line
col=[]#min column
new=[[],[],[]]

ffunc.dell(num,col,mi,new,n,i)
ffunc.column(new,col)




print(n,num[0],n,num[1],n,num[2])	
print(n,'Min numbers of line(рядок):',mi,n,'Min num of column(стовпець)',col)
#new=[[0,1,2],[3,4,5],[6,7,8]]
#print(n,new[:3],n,new[3:6],n,new[6:9])
print(n,'after reducing',n,new[0],n,new[1],n,new[2])