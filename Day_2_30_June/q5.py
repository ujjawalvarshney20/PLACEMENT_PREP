nums=list(map(int,input('nums:').split(' ')))
c=0
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if(nums[i]==nums[j]):
            c+=1
            #print(i,j)
print(c)