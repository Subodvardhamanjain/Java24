def bubblesort(a):
    for i in range(len(a)):
        for j in range(0,len(a)-i-1):
            if a[i]>a[j+1]:
                temp=a[j]
                a[i]=a[j+1]
                a[j+1]=temp
a=[2,34,1,88,77]                
bubblesort(a)               
print(a) 
