nums=[1,2,3,4,5,6,7,8,9]
temp=0
sum=[]
for i in range(0,len(nums)):
    temp=temp + nums[i]
    sum.append(temp)
print(sum)
