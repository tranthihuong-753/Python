""" 
Bài tập 3. Cho mảng a các số nguyên. Yêu cầu sắp xếp mảng a theo thứ tự không giảm 
và in kết quả lên màn hình; 
sắp xếp mảng a theo dạng sóng.
Ví dụ dạy có dạng sóng: 1 10 -20 0 50 -20 8 4
"""

arr = [1, 10, -20, 0, 50, -20, 8, 4]
""" 
Xắp xếp tăng dần 
"""
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
arr = quicksort(arr, 0, len(arr)-1)
print(f"Mang sau khi xap xep khong giam la : \n{arr}")
""" 
Hiển thị dạng sóng của mảng không giảm theo đầu-cuối không được khi 1 2 3 3 4 5 
"""

""" 
Hiển thị dạng sóng của mảng không giảm đầu-giữa 
"""
def songdaucuoi(arr):
    n = len(arr)
    i = 1
    indexgiua = int(n/2 - (n/2)%1 )
    while indexgiua < n:
        print(f"i={i}, indexgiua={indexgiua}")
        x = arr[i]
        arr[i] = arr[indexgiua]
        arr[indexgiua] = x
        print(arr)

        i += 2
        indexgiua += 2 
    return arr 

print("Mang chuyen sang song la : \n", songdaucuoi(arr))

