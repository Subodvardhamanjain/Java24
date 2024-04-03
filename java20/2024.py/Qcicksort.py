import random
def partition(arr,i,j):
    pivot=arr[i]
    
    left=i+1
    right= j
    while True:
        while left <= right and arr[left] < pivot:
            left=left+1
            while right >= left and arr[right] >= pivot:
                right=right-1
          
            else:
                break


        arr[i],arr[right]=arr[right],arr[i]
        return right
    
def QuickSort(arr,i,j):
        if i>=j:
            return
        pos = partition(arr,i,j)
        QuickSort(arr,i,pos -1)
        QuickSort(arr,pos +1,j)

n=int(input("Enter the number of element: "))
arr=list()
for i in range(n):
    k=random.randint(10,99)
    arr.append(k)

    QuickSort(arr,0,len(arr)-1)
    print("Sorted list is",arr)                                        