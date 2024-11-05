""" 
Bài tập 1: Nhập vào số nguyên dương. Phân tích số đó thành tích các số nguyên tố 
và in lên màn hình. 8 = 2*2*2
"""

""" def check_songuyento(a):
    i = 2
    can_a = int(a**(1/2))
    if a<=0:
        return False 
    while i<can_a:
        if(a%i == 0):
            return False
        i += 1
    return True
a = int(input("Nhap vao so muon check: "))
print(check_songuyento(a)) """

def tinhsonguyentotieptheo(a):
    print("ham moi")
    while a%2 == 0:
        print("2*", end="")
        a=a//2
    
    sobichia = 3
    while a!=1:
        if a%sobichia == 0:
            print(f"{sobichia}*", end="")
            a = a//sobichia 
        else:
            sobichia += 2 

def tinhsonguyentotieptheo1(a):  
    print("ham cu")
    sobichia = 2
    while a!=1:
        if a%sobichia == 0:
            print(f"{sobichia}*", end="")
            a = a//sobichia
        else:
            sobichia += 1

a=12345678910111
tinhsonguyentotieptheo1(a)
print()
tinhsonguyentotieptheo(a)

