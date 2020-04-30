#Матриця на 3 міста Львів, Київ, Черкаси,+ще одне місто для реал. другого етапу
from math import inf
import ffunc
#import trn2

i=inf;n='\n'

num=[[i,1,4,8],[8,i,2,4],[4,9,i,6],[10,8,5,i]]
new=[[] for y in num]
new1=[[] for y in num]

print('Origin:',n,num[0],n,num[1],n,num[2],n,num[3])
mi=list(map(lambda x:min(x),num))#min line
print(n,'Min numbers of line(рядок):',mi)


ffunc.dell(num,mi,new)#reducing lines
print(n,'after reducing lines',n,new[0],n,new[1],n,new[2],n,new[3])

col=[min(x) for x in zip(*new)]#min column
print(n,'Min num of column(стовпець)',col)
ffunc.dell2(col,new1,new)#reducing columns
print(n,'after reducing columns',n,new1[0],n,new1[1],n,new1[2],n,new1[3],n,n)


print('МЕТОД ШТРАФІВ!!!!!')

#shtr.shtr(new1,n,i,)

#####################################Тоже цікаво
SUMA=sum(mi)+sum(col)
print(n,'Сума констант редукції:',SUMA)



####Etap 2
#shtr(new1)