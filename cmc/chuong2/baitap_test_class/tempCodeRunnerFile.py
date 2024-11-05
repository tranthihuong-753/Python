import pandas as pd

data = pd.read_csv("D:\CMC_Ky4\CODE\Python\cmc\chuong2\\baitap_test_class\data.csv")
print(data)

""" 
        Năm  ...  Lợi nhuận
0      1955  ...        806
1      1955  ...      584.8
2      1955  ...      195.4
3      1955  ...      212.6
4      1955  ...       19.1
...     ...  ...        ...
25495  2005  ...        493
25496  2005  ...      175.4
25497  2005  ...       57.8
25498  2005  ...       70.6
25499  2005  ...        584

[25500 rows x 5 columns]
 """

print(data.dtypes)
""" 
Năm            int64
Xếp hạng       int64
Công ty       object
Doanh thu    float64
Lợi nhuận     object
dtype: object
 """

print(len(data))
