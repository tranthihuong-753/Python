""" Tải thư viện pandas thông qua terminal  """
""" 1. Series """
import pandas as pd 
""" TAO 1 SERIES """
""" Tạo series object bằng mảng """
arr = ["chó", "mèo", "cá"]
s = pd.Series(arr)
print(s)
""" 
0    chó
1    mèo
2     cá
dtype: object 
"""

""" Tạo series int bằng từ điển index:values"""
dict = {'a':1, 'b':2, 'c':3}
s_dict = pd.Series(dict)
print(s_dict)
""" 
a    1
b    2
c    3
dtype: int64
"""
print(f"{s_dict.index} | {s_dict.values}")
""" Index(['a', 'b', 'c'], dtype='object') | [1 2 3] """

list = ["Tran Huong", 19, 1.2]
s_list = pd.Series(list)
print(s_list)
""" 
0    Tran Huong
1            19
2           1.2
dtype: object
 """

""" TAO 1 DATAFRAME = nhieu series"""
list1 = ["Tran Huong", "Trang Di", "Thu"]
list2 = [19, 19, 18]
list3 = [1.2 , 2.3 , 3.4]
d_list = pd.DataFrame({
    "name": list1,
    "age": list2,
    "point":list3
})
print(d_list)
""" 
         name  age  point
0  Tran Huong   19    1.2
1    Trang Di   19    2.3
2         Thu   18    3.4
 """
print("Danh sach name (cot 1): ")
print(d_list['name'])
""" 
0    Tran Huong
1      Trang Di
2           Thu
"""

print("Danh sach")
print(d_list.iloc[0])
""" 
name     Tran Huong
age        Trang Di
point           Thu
Name: 0, dtype: object
 """

