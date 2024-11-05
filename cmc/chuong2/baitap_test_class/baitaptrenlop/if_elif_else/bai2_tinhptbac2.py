""" Cho 3 số a, b, c là các hệ số của Phương trình ax2
 + bx + c = 0. Tính và in kết quả của phương trình. """

def giaiptbac2(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "vo so nghiem"
            else:
                return "vo nghiem"
        else:
            return f"x = {-c/b}"
    else:
        dt = (b**2) - 4*a*c
        if dt < 0 :
            return "vo nghiem"
        elif dt == 0:
            return f"nghiem kep x = {-b/(2*a)}"
        else:
            can_dt = dt**(1/2)
            return f"2 nghiem phan biet x1 = {(-b + can_dt)/(2*a)} x2 = {(-b - can_dt)/(2*a)} "
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
print(giaiptbac2(a, b, c))