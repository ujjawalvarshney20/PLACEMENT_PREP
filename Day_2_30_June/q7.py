accounts=[]
for i in range(int(input('No of customer:'))):
    accounts.append(list(map(int,input('Customer '+str(i+1)+':').split(' '))))
l=[]
for i in accounts:
    l.append(sum(i))
print(max(l))