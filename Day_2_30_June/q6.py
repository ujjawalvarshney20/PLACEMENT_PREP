chocolates=list(map(int,input('Chocolates:').split(' ')))
extraChocolates=int(input('Extra:'))
m=max(chocolates)
l=[]
for i in chocolates:
    #print(i+extraChocolates,m)
 if(i>=(m-extraChocolates)):
    l.append(True)
 else:
    l.append(False)
    
    print(l)