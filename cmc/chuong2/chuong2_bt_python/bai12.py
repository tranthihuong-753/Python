""" Mang 2 chieu """

m = int(input("Nhap vao chieu thu nhat cua mang : "))
n = int(input("Nhap vao chieu thu hai cua mang :"))
arr = []
for i in range(0, m):
    e = []
    for j in range(0, n):
        e.append(float(input(f"Nhap vao gia tri cua phan tu {i}{j} : ")))
    arr.append(e)

print("Mang nhap vao : " , arr)

for e in arr:
    e.sort()

print("Mang sau khi sap xep : " , arr)
