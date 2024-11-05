""" 
link : https://www.youtube.com/watch?v=-c2mdgE_epw&list=PLPt6-BtUI22oGqQwAEF6xwrFL6aOjtHWl&index=21
"""

""" 1:40 """
""" Xuat bang cuu chuong han cua 2, 3 """
""" 2 <= a <= 9 ; b = {+, -, *, /} """
""" 
def print_bangcuuchuong(a, b):
    if b == '+':
        for i in range(1, 11, 1):
            print(f"{a} + {i} = {a + i}")
    elif b == '-':
        for i in range(1, 11, 1):
            print(f"{a} - {i} = {a - i}")
    elif b == '*':
        for i in range(1, 11, 1):
            print(f"{a} * {i} = {a * i}")
    elif b == '/':
        for i in range(1, 11, 1):
            print(f"{a} / {i} = {a / i}")

print_bangcuuchuong(2, '*')
"""

""" 9:08 """
def tym():
    print("Hinh trai tim")
    for i in range(0, 7, 1):
        for j in range(0, 7, 1):
            if (i == 0 and (j == 1 or j == 2 or j == 4 or j ==5)) or (i == 1 and (j == 0 or j == 3 or j == 6 )) or (i == 2 and (j == 0 or j == 6)) or (i == 3 and (j == 1 or j ==5)) or (i == 4 and (j == 2 or j == 4) or (i == 5 and j == 3)):
                print("   *   ", end="")
            else : 
                print("       ", end="")
        print()
tym()
