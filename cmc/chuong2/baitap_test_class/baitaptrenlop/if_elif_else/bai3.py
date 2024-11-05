""" Nhập vào 3 số a, b, c. In lên màn hình 3 số đó có tạo thành 3 cạnh của 1 tam giác hay không?"""

def check(a, b, c):
    if((a<(b + c)) and (a > (b - c) or a > (c - b))):
        return True
    else:
        return False

def check_tg(a, b, c):
    return check(a, b, c) and check(a, c, b) and check(b, a, c) and check(b, c, a) and check(c, a, b) and check(c, b, a)

def chuvi(a, b, c):
    return a+b+c

def dientich(a, b, c):
    x = chuvi(a, b, c)/2
    return (x*(x-a)*(x-b)*(x-c))**(1/2)

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if(check_tg(a, b, c) == True):
    print("La tam giac")
    print(f"chu vi {chuvi(a, b, c)}")
    print(f"dien tich {dientich(a, b, c)}")
else:
    print("Khong la tam giac")

    