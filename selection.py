def selectionSort(arr):
    n=len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    
elements=[]
for i in range(6):
    element=int(input("enter your numbers"))
    elements.append(element)
    print("unsorted lit",elements)
    selectionSort(elements)
    print("sorted list",elements)



