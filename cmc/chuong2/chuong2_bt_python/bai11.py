n = int(input("Nhap vao so luong phan tu cua mang: "))

a = []

sum_le = 0

for i in range(0, n):
    e = float(input(f"Nhap vao gia tri phan tu thu {i+1} : "))
    a.append(e)
    if i % 2 == 0 : 
        sum_le += e 

print(a)
print(f"Tong so o v tri le la : {sum_le}")
