""" 2. Nhập vào ba số a, b và c, yêu cầu tìm số lớn nhất trong ba số đó rồi in
kết quả lên màn hình. """


def searchmax(a, b, c):
    max = a 
    if b > max : 
        max = b 
    if c > max :
        max = c
    return max 

a = float(input("Nhap vao so thu nhat : "))
b = float(input("Nhap vao so thu hai :"))
c = float(input("Nhap vao so thu ba : "))

print(f"Max cua ba so {a} ; {b} ; {c} la {searchmax(a, b, c)}")