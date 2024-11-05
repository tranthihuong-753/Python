a = int(input("Nhap vao so nguyen a : "))

while a!=1 : 
    if a%2 == 0 :
        a /= 2
    else :
        a = 3*a + 1 

print("Hoan thanh.") 