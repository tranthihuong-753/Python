""" Bài toán phải sử dụng while """ 

def hdinput():
    a = input("Nhập vào password laptop của bạn: ")
    while a != "kieuolaungungbich":
        print("Bạn ngu lắm")
        a = input("Nhập vào password laptop của bạn: ")      

def nhapmang():
    arr = [0] * 10 
    i = 0
    print("Luat : So thu tu le thi duong, chan thi am.")
    while i < 10:
        arr[i] = int(input(f"Nhap vao mot so co thu tu {i+1}: "))
        if i%2 == 0:
            while arr[i] < 0:
                arr[i] = int(input(f"Nhập vào số nguyên dương có số thứ tự {i+1}: "))
                
        else:
            while arr[i] >= 0:
                arr[i] = int(input(f"Nhập vào số nguyên âm có số thứ tự {i+1}: "))
        i += 1 
    return arr

print(nhapmang()) 
