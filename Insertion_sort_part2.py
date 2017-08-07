#!/bin/python
def insertionSort(ar):   
    for i in range(1,len(ar)):
        ele = ar[i]
        while ele < ar[i-1] and i > 0:
            ar[i] = ar[i-1]
            ar[i-1] = ele
            i -= 1
            # print ar
        print ' '.join(str(i) for i in ar)
    #return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)

#input
#6
#1 4 3 5 6 2

#output
#1 4 3 5 6 2 
#1 3 4 5 6 2 
#1 3 4 5 6 2 
#1 3 4 5 6 2 
#1 2 3 4 5 6 
