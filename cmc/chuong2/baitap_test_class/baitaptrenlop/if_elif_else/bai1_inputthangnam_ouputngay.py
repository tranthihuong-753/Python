""" Nhập vào tháng và năm dương lịch nào đó. Hiện lên kết quả tháng đó có bao nhiêu ngày? """

a = int(input("Thang bat ky: "))
b = int(input("Nam bat ky: "))

def check_namnhuan(b):
    return b%4==0 and y%100!=0

def travangay(a, b):
    if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
        return 31
    elif a==2:
        if check_namnhuan(b):
            return 29
        else:
            return 28
    else:
        return 30 

print(f"ngay {travangay(a, b)}")
