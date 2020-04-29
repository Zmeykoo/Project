from math import inf
n='\n'
i=inf
spi=[[i,0,4,8],[0,i,2,4],[4,9,i,0],[10,8,0,i]]
print('Origin:',n,spi[0],n,spi[1],n,spi[2],n,spi[3],n)
col=[list(f) for f in zip(*spi)]
#print('column:',n,col[0],n,col[1],n,col[2],n,col[3])
##############
inde=[]
for x in spi:		
	inde.append(x.index(min(x)))
	#print('min x:',min(x),'(index)=',x.index(min(x)))
print(n,'Index*s min x:',inde,n,'################',n)

##############
lines=[[] for x in spi]
nu=0
for j in spi:
	for x in j:
		if x!=i: 
			lines[nu].append(x)
		else:
			x=0
			lines[nu].append(x)
	nu+=1

#print('lines:',n,lines[0],n,lines[1],n,lines[2],n,lines[3],n)
col=[list(f) for f in zip(*lines)]
#print('column:',n,col[0],n,col[1],n,col[2],n,col[3])

def suum(l,c,s):
	sumal=[sum(k) for k in l]
	sumac=[sum(f) for f in c]
	sumaa=[]
	miline=[[] for x in spi]
	micol=[[] for x in spi]
	a=0
	def milc(s,l,c):
		nu=0
		for x in spi:
			fk=x[inde[nu]]
			x[inde[nu]]=i
			print(inde[nu],x[inde[nu]],fk,i)
			nu+=1
		print('Origin:',n,spi[0],n,spi[1],n,spi[2],n,spi[3],n)
##################################################################################
		nu=0
		l=[min(f) for f in spi]
		c=[min(f) for f in zip(*spi)]
		print(n,'min lines',l,n,'min colum',c)
	milc(s,l,c)
	miline=[min(x) for x in s]
	#print(n,l,n,c)
	print()
	print(n,sumal,'- lines',n,sumac,'- columns',n,n)
suum(lines,col,spi)
