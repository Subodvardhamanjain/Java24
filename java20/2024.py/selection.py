def SelectionSort(a):
    for i in range(len(a)):
        for j in range(i,len(a),++1):
            if a[i]>a[j]:
                a[j],a[i]=a[i],a[j]
            print(a)                