"""
Nhập vào số nguyên dương n 
  Check có phải số hoàn thiện hay không 
    bằng tổng các ước của số a = số a thì a là số hoàn thiện 
In ra màn hình  
"""

def checksohoanthien(n):
    sum = 1
    x = 2
    while x < n/2:
        if n%x == 0:
            sum += x
            sum += (n/x)
        x+=1
    if sum == n :
        return True 
    return False 

n = int(input("Nhâp vào số nguyên dương n: "))
print(f"Check số hoàn thiện {n} : {checksohoanthien(n)}")
