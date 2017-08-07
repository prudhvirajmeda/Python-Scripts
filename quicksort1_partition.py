#!/bin/python
def partition(ar):  
    pivot = ar[0]
    left_list = []
    right_list = []
    equals = []
    for i in ar:
        if i < pivot:
            left_list.append(i)
        elif i == pivot:
            equals.append(i)
        elif i > pivot:
            right_list.append(i)
    for i in range(1,len(left_list)):
        ele = left_list[i]
        while i > 0  and left_list[i-1] > ele:
            left_list[i]= left_list[i-1]
            left_list[i-1] = ele
    new_list = left_list+equals+right_list
    return ' '.join(str(i) for i in new_list )

m = input()
ar = [int(i) for i in raw_input().strip().split()]
print partition(ar)

# Sample Input

# 5
# 4 5 3 7 2
# Sample Output

# 3 2 4 5 7
