import random
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


#Exanmple usage
n=int(input("Enter the number of element: "))
arr=list()
for i in range(n):
    k=random.randint(10,99)
    arr.append(k)
    print(quicksort(arr))   