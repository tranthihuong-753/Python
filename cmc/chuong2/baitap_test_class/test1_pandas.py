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
""" 
25500
"""

print(data["Công ty"])
""" 
0               General Motors       
1                  Exxon Mobil       
2                   U.S. Steel       
3             General Electric       
4                       Esmark       
                 ...
25495          Wm. Wrigley Jr.       
25496           Peabody Energy       
25497    Wendy's International       
25498       Kindred Healthcare       
25499     Cincinnati Financial       
Name: Công ty, Length: 25500, dtype: object
"""

print(data.iloc[1])
""" 
0               General Motors       
1                  Exxon Mobil       
2                   U.S. Steel       
3             General Electric       
4                       Esmark       
                 ...
25495          Wm. Wrigley Jr.       
25496           Peabody Energy       
25497    Wendy's International       
25498       Kindred Healthcare       
25499     Cincinnati Financial       
Name: Công ty, Length: 25500, dtype: object
"""

""" 
data[data["Lợi nhuận"] > 500].head()
Run lỗi lòi vì cột "Lợi nhuận" đang kiểu object 
"""

data["Lợi nhuận"] = pd.to_numeric(data["Lợi nhuận"], errors='coerce')
print(data[data["Lợi nhuận"] > 500].head())
""" 
       Năm  ...  Lợi nhuận
0     1955  ...      806.0
1     1955  ...      584.8
500   1956  ...     1189.5
501   1956  ...      709.3
1000  1957  ...      847.4

[5 rows x 5 columns]
"""

""" Tính trung bình lợi nhuận """
def tb_loinhuan(a):
    tongloinhuan = 0
    so_bi_chia = 0
    for x in a:
        if pd.notna(x):  # Không NaN 
            tongloinhuan += x
            so_bi_chia += 1
    if so_bi_chia == 0:  # Tránh chia cho 0
        return 0
    return tongloinhuan / so_bi_chia
print(f"Loi nhuan trung binh la {tb_loinhuan(data['Lợi nhuận'])}")
""" 
Loi nhuan trung binh la 207.9036767339139
"""
print(f"Loi nhuan trung binh la {data['Lợi nhuận'].mean()}")
""" 
Loi nhuan trung binh la 207.9036767339139
"""

""" Xắp xếp dữ liệu giảm dần theo lợi nhuận t39 """

