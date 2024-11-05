def quicksort(arr, head, tail):   
    pivot = tail
    i = head   
    """ i != pivot bi loi tum lum """
    while i < pivot:
        if arr[i] > arr[pivot]:
            x = arr[i]
            arr[i] = arr[pivot-1]
            arr[pivot-1] = x
            
            y = arr[pivot-1]
            arr[pivot-1] = arr[pivot]
            arr[pivot] = y
            
            pivot -= 1
        else:
            i += 1  
    if tail>head:
        quicksort(arr, head, pivot-1)
        quicksort(arr, pivot+1, tail)    
    return arr

arr = [2, 4, 3, -3, 2, 5, -5, 4, 6]
print(quicksort(arr, 0, len(arr)-1))
