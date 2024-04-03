import random
def mergesort(arr):
    if (len(arr))>1:
        mid=int(len(arr)/2)
        L=arr[:mid]
        y=len(L)
        R=arr[mid:]
        z=len(R)
        mergesort(L)
        mergesort(R)
        i=0
        j=0
        k=0
        while i<y and j<z:
            if L[i]<=R[j]:
                arr[k]=L[i]
                i=i+1
                k=k+1
            elif L[i]>R[j]:
                arr[k]=R[j]
                j=j+1
                k=k+1
                
        while i< y:
            arr[k]=L[i]
            k=k+1
            i=i+1
        while j<z:
            arr[k]=R[j]
            k=k+1
            j=j+1
#main code
arr=[]
n=int(input("Enter ther no of elements:"))
for i in  range(n):
    num=random.randint(1,99)
    arr.append(num)
print("Before the sort")
print(arr)
mergesort(arr)
print("after sort")
print(arr)  