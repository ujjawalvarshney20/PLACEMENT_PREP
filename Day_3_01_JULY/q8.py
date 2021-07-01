 target = [0]*(len(nums)-1)
    for i in range(len(nums)):
        target.insert(index[i],nums[i])
    return target[:len(nums)]