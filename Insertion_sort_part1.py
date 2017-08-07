#!/bin/python
def insertionSort(ar):   
    ele = ar[-1]
    index = len(ar)-2
    while ar[index] > ele and index !=-1:
        ar[index+1]=ar[index]
        index -= 1
        print ' '.join(str(i) for i in ar)
    ar[index+1] = ele
    print ' '.join(str(i) for i in ar)
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)

#Sample Input

#5
#2 4 6 8 3

#Sample Output

#2 4 6 8 8 
#2 4 6 6 8 
#2 4 4 6 8 
#2 3 4 6 8 
