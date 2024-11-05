""" Nhập vào số nguyên a, in lên màn hình số đó có phải số chính phương hay không? """

def checksochinhphuong(a):
    if a <= 0:
        return "Khong la so chinh phuong"
    b = a**(1/2)
    if (b%1)==0 :
        return "La so chinh phuong"
    else :
        return "Khong la so chinh phuong"

a = float(input("Nhap vao so muon check: "))
print(checksochinhphuong(a))
