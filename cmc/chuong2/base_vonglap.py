for i in range(3):
    print(i) 
    """ 0 1 2  """

arr = ["i", "love", "me"]
for x in arr:
    print(x)
""" 
i
love
me 
"""

i = 0
while i < 3 :
    print(i)
    i += 1 
    """ 0 1 2  """

""" No i++ """

""" Hàm tính tổng mảng số nguyên """
def add_num(a):
    tong = 0
    for x in a:
        tong += x
    print(tong)

arr=[1, 2, 3]
add_num(arr) 
""" 6 """

