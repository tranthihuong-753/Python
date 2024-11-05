def tinhgiaithua(n):
    if n < 0 :
        return "So nhap vao khong hop le"
    out = 1 
    for i in range(2, n + 1):
        out *= i 
    return out 

n = int(input("Nhap vao gia tri cua so muon tinh giai thua "))
print(f"{n}! = {tinhgiaithua(n)}")
