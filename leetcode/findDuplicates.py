
nums=[0,1,2,3,4,0]

def checkDuplicate(nums):
    i=0
    j=0
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                return True
            j+=1
        i+=1    
    return False
print(checkDuplicate(nums))