""" nhập vào 3 số , tìm số lớn nhất """

def timmax(a, b, c):
    max = a
    if max < b:
        max = b
    if max < c :
        max = c 
    return max 

a = float(input("Nhap vao so thu nhat: "))
b = float(input("Nhap vao so thu hai: "))
c = float(input("Nhap vao so thu ba: "))
print(f"Max cua ba so {a} ; {b} ; {c} la {timmax(a, b, c)}")
