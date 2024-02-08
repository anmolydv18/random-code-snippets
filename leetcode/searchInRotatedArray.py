# have to do this by binary search instead of this approach
nums=(4,5,6,7,0,1,2)
target=0
if target in nums:
    index=nums.index(target)
    print(index)
else:
    print("-1")