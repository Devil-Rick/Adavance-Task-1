"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""

array = list(map(int, input().split(',')))
n = len(array)//2
split_list = [array[i:i+n] for i in range(0, len(array), n)]
out = []
for i in range(1, len(array)+1):
    if i % 2 != 0:
        out.append(split_list[0][0])
        split_list[0].pop(0)
    else:
        out.append(split_list[1][0])
        split_list[1].pop(0)
print(out)
