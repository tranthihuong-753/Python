""" Cho xâu ký tự có dộ dài n, chứa full STN 0 -> 9
Xóa đi k số (k < n) để số trong xâu max
 """

s = input("Nhap vao chuoi so ban dau : ")
arr = [int for int in s]
print(arr)
k = int(input(f"Nhap vao so luong phan tu muon xoa (Luu y nho hon {len(s)}) : "))

def delete(arr, k):
    count = 0 
    while count < k : 
        i = 0 
        check = False
        while i < (len(arr) - 1):
            if arr[i] <= arr[i + 1]:
                del arr[i]
                check = True
            i += 1 
            """ Chú ý check vì nếu không có if thì check vo dụng """
            if check == True :
                break 
            if i == (len(arr) - 1) :
                del arr[i]
        count += 1 
    return arr 

print(f"{delete(arr, k)}")
