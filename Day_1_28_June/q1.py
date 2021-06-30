n = len(nums)
        if(n==0 or n==1):
            return n
        c=1
        for i in range(1,n):
            if(nums[i]!=nums[i-1]):
                nums[c]=nums[i]
                c+=1
        return c
