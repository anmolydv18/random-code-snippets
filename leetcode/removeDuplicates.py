i = 0
j = 1
nums = [1, 1, 2, 3, 3, 4,4,4,4,5,6,7,8,9,9]
newnum = []

while j < len(nums):  # Use '<' instead of '<=' to avoid IndexError
    if nums[i] == nums[j]:
        i+=1
        j += 1  # Move to the next element without appending to newnum
    else:
        newnum.append(nums[i])
        i += 1
        j += 1

# Add the last element (if any) to newnum
if i < len(nums):
    newnum.append(nums[i])
nums[:]=newnum[:]
print(nums)
print(newnum)