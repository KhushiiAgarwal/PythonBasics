# Given an array of numbers and a target integer, find two elements from the array that sums up to target. Return the indices of these two elements (0-based).
# The pair of indices returned should be sorted. If multiple such indices exist, break ties by returning the pair with the left-most first index.
# If there are still multiple such pair with same first indices, return the pair with the left-most second index. If there is no pair that sums to target, return an empty array.

nums =list(map(int,input("Enter list:").split()))
res=[]
target = int(input())
flag = 0
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        sum_n = nums[i] + nums[j]
        if sum_n == target:
            res.append(i)
            res.append(j)
            flag = 1
    if flag== 1:
        break
print(res)
