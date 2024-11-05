n = int(input("Nhap vao gia tri n de tinh f(n) : "))

S = 0 
for i in range(1, n+1):
    S += 1 / i 

print(f"Gia tri cua f({n}) = {S}")