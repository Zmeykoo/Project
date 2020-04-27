import ffunc
ent=list(input("Enter cities:").split(','))
#spis=[ent[i][0].upper();ent[i][1:].lower() for i in range(len(ent))
spis=list(map(ffunc.bigsmall,ent))
city=['Lviv','Kyiv','Odesa','Belz','Sumy','Chg']
n='\n'
##цикл, що шукає збіги між списком введеним користувачем і заданим списком. Також не допускає міста введені двічі 
#for i in spis:
#	if i in ch:
#		continue
#	for j in city:
#		if i==j:
#			ch.append(i)
#			break
##той самий спосіб, тільки з перетворенням списків в множини і порівняння їх за допомогою функції set
ch=list(set(spis)&set(city))
print(n,spis,'- cities entered by user',n,city,'- all access cities',n,ch,'- cities to run\n')
