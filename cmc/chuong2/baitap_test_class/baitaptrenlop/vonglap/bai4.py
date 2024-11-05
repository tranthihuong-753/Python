""" 
Bài tập 4. Cho mảng a các số nguyên, yêu cầu tính trung bình cộng các số dương,
trung bình cộng các số chính phương và in lên màn hình.
"""

def check_sochinhphuong(a):
    if a<=0 :
        return False 
    if (a**(1/2))%1 == 0 :
        return True
    else:
        return False 

def demo(arr):
    tongsoduong = countsoduong = tongsochinhphuong = countsochinhphuong = countarr = 0
    n = len(arr)
    while countarr < n:
        if arr[countarr] > 0:
            tongsoduong += arr[countarr]
            countsoduong += 1 
        if check_sochinhphuong(arr[countarr]):
            tongsochinhphuong += arr[countarr]
            countsochinhphuong += 1 
        countarr += 1
    if countsoduong != 0 :
        print(f"TBC so duong = {tongsoduong/countsoduong}")
    else:
        print("Khong co so duong")
    if countsochinhphuong != 0 :
        print(f"TBC so duong = {tongsochinhphuong/countsochinhphuong}")
    else:
        print("Khong co so chinh phuong")

arr = [1, 10, -20, 0, 50, -20, 8, 4, 3]
demo(arr) 
