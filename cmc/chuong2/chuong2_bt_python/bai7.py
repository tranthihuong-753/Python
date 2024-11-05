def checksonguyento(n):
    if n <= 1 :
        return False
    for i in range(2, n//2 +1):
        if n % i == 0 :
            return False 
    return True 

n = int(input("Nhap vao gia tri cua so muon kiem tra: "))
print(f"{checksonguyento(n)}")
