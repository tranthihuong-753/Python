import matplotlib 
import pandas as pd 

data = pd.read_csv("chuong2\\baitap_test_class\data.csv")
""" Phải dùng đường dẫn đầy đủ, có thẻ folder cha là folder lớn nhất được mở mà chứa file đang thực thi """
print(data)

revenue_per_year = data.groupby('Năm')['Doanh thu'].mean()

plt.figure(figsize=(10, 6))
plt.plot(revenue_per_year.index, revenue_per_year.values, marker='o', linestyle='-', color='b')

plt.title('Biểu đồ Doanh thu trung bình theo Năm', fontsize=16)
plt.xlabel('Năm', fontsize=14)
plt.ylabel('Doanh thu trung bình (triệu USD)', fontsize=14)

plt.show()


