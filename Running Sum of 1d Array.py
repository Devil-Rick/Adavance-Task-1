"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""

array = list(map(int, input().split(',')))
out = []
s = 0
for i in array:
    x = s+i
    out.append(x)
    s = x
print(out)
