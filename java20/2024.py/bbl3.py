import time
import numpy as np
import matplotlib.pyplot as plt
def bubblersort (arr):
    for i in range (len(arr)):
        for j in range (0,len(arr)-i-1):
            if arr[i]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
times=list()
arr=list()
numtimes=list()
for i in range(1,8):
    start=time.time()
    n=int(input("Enter the no of element"))
    numtimes.append (n)
    for x in range(n):
        number=np.random.randint(10,99)
        arr.append(n)
    print("List before sorting",x+1,"Element")
    print(arr)
    bubblersort(arr)
    end=time.time()
    times.append(end-start)
    print("list after bubblesort of",x+1,"element")
    print(arr)
    bubblersort(arr)
    print("time taken for bubblr sort for",n,"element is",end-start)
    print(numtimes)
    print(times)
    plt.xlabel('list length')
    plt.ylabel('time complexity')
    plt.plot(numtimes,times,leble="bubblesort")
    plt.grid()
    plt.legend()
    plt.show()