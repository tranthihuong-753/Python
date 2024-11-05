def bubblesort(arr):
    n = len(arr)
    """ Do dai mang """
    while n!=1:
        check = False 
        """ Khong con su thay doi trong so phan tu tu 0 den i dang xet """
        for i in range(0, n - 2):
            if arr[i] > arr[i+1]:
                x = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = x 
                check = True
        if check == False:
            break 
        n -= 1
    return arr

arr = [2, 4, 3, 4, 2, 5, -5, 4, 4, 5, 6, 6]

print(f"mang sau khi sap xep tang dan la : {bubblesort(arr)}")
