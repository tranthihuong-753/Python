n = int(input("Nhap vao so phan tu cua mang : "))

print(f"Nhap vao gia tri cac phan tu cua mang {n} phan tu ")

a = []

for i in range(n):
    a.append(float(input(f"Nhap vao phan tu thu {i+1} : ")))

print("Mang cua nhap " , a)

def tbc_chan(arr):
    sum = 0
    for e in arr :
        if e % 2 == 0 :
            sum += e 
    return sum 

print(f"TBC cac phan tu chan cua mang la {tbc_chan(a)}")

def checksochinhphuong(e):
    if e <= 0 :
        return False 
    if (e**(1/2))%1 != 0 :
        return False 
    return True 

print("Cac so chinh phuong co trong mang la : ")
for e in a : 
    if checksochinhphuong(e):
        print(f"    {e}")
    
