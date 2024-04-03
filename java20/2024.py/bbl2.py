arr= [4,5,6,7,9,]
for i in range(len(arr)):
    for j in range(0,len(arr)-i-1):
        if arr[i] > arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
           
print(arr)

import time
def bubble_sort(arr):
    n=len(arr)
    swapped =True
    while swapped:
        swapped=False
        if arr[i-1]>arr[i]:
            arr[i-1],arr[i]=arr[i],arr[i-1]
            swapped=True
    n-=1
arr=[4,5,6,1,-1,7,9]
print("Original array:",arr)
Star_time=time.time()
bubble_sort(arr)
end_time=time.time()
print("Sorted array:",arr)
print("Execution:",end_time-Star_time,"seconds")