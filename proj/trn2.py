from math import inf
n='\n'
i=inf
inde=[]
cycle=[]
spi=[[i,0,4,8],[0,i,2,4],[4,9,i,0],[10,8,0,i]]
print('Origin:',n,spi[0],n,spi[1],n,spi[2],n,spi[3],n)

def milc(s,inde):
	""" 1)Виявлення нулів та їх індексів для штрафування,
 2)заміна штрафів на inf,
 3)штрафування,
 4)пошук найбільшого штрафа
 5)видалення рядка і стовпця найбільшого штрафа"""
	print (milc.__doc__)
	
	for x in spi:		
		inde.append(x.index(min(x)))
	print(n,'Виявлення нулів та їх індексів для штрафування')
	nu=0
	for x in spi:
		fk=x[inde[nu]]
		x[inde[nu]]=i
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
	c=[list(f) for f in zip(*spi)]
	print(c,n,'Штрафування',n,spi[0],n,spi[1],n,spi[2],n,spi[3],n)
	bs=max(bs)
	print('Найбільший штраф =',bs,n)
	def rem(s,inde,bs,c):
		nu=0
		kilc=[]
		def kill(s,c,k):
			"""Видалення рядка і стовпця найбільшого штрафа"""
			print(kill.__doc__)
			print('Індекси рядка і стовпця штрафа {}'.format(k))
			del s[k[0]]
			c=[list(f) for f in zip(*s)]
			del c[k[1]]
			s=[list(f) for f in zip(*c)]
			def notcycle(k,s):
				"""Функція міняє обернене розположення штрафа на inf,
 це допомагає уникнути зациклення"""
				print(n,notcycle.__doc__,n)
				#k=[3,1]
				print('k =',k)
				if k[0]<k[1]:
					k[1]-=1
					#print('\nk[1]-1\n')
				elif k[0]>k[1]:
					k[0]-=1
					#print('\nk[0]-1\n')
				k.reverse()
				cycle.append(k)
				s[k[0]][k[1]]=i
				print('cycle=',cycle)
			notcycle(k,s)
			print(n,s[0],n,s[1],n,s[2],n)
			
		for x in range(len(s)):
			if bs in spi[x]:
				print('Bie bie',spi[x])
				kilc.append(s.index(s[x]))
			if bs in c[x]:
				print('Bie bie',c[x])
				kilc.append(c.index(c[x]))
		kill(s,c,kilc)
	rem(s,inde,bs,c)
milc(spi,inde)

