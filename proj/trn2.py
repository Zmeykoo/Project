from math import inf
n='\n'
i=inf
inde=[]
spi=[[i,0,4,8],[0,i,2,4],[4,9,i,0],[10,8,0,i]]
print('Origin:',n,spi[0],n,spi[1],n,spi[2],n,spi[3],n)

def milc(s,inde):
	""" 1)Виявлення нулів та їх індексів для штрафування,
 2)заміна штрафів на inf,
 3)штрафування,
 4)пошук найбільшого штрафа"""
	print (milc.__doc__)
	
	for x in spi:		
		inde.append(x.index(min(x)))
	print(n,'Виявлення нулів та їх індексів для штрафування')
	nu=0
	for x in spi:
		fk=x[inde[nu]]
		x[inde[nu]]=i
		#print(fk,'=',inde[nu],'index')
		print(' {} = {} index'.format(fk,inde[nu]))
		nu+=1
	print(n,'Origin after changes(заміна штрафів на inf):',n,spi[0],n,spi[1],n,spi[2],n,spi[3],n)

	bs=[]
	col=[list(f) for f in zip(*spi)]
	nu=0
	for x in s:
		x[inde[nu]]=min(x)+min(col[inde[nu]])
		bs.append(x[inde[nu]])
		nu+=1
	print('Штрафування',n,spi[0],n,spi[1],n,spi[2],n,spi[3],n)
	bs=max(bs)
	print(bs)
	def rem(s,inde,bs):
		for x in spi:
			
	rem(s,line,bs)
milc(spi,inde)
