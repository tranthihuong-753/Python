import os
import numpy as np
import matplotlib.pyplot as plt

# Đường dẫn đến thư mục chứa dữ liệu
data_dir = 'D:\CMC_Ky4\CODE\Python\cmc\chuong4_CNN\PhanLoaiSoVoiMNIST\data'

# Tải dữ liệu từ các file đã lưu
x_train = np.load(os.path.join(data_dir, 'x_train.npy'))
y_train = np.load(os.path.join(data_dir, 'y_train.npy'))
x_test = np.load(os.path.join(data_dir, 'x_test.npy'))
y_test = np.load(os.path.join(data_dir, 'y_test.npy'))

print("Số mẫu trong x_train ", x_train.shape[0]) # 60.000
print("Số mẫu trong x_test ", x_test.shape[0])  # 10.000 

# Giảm bớt số lượng dữ liệu
x_train = x_train[:1000]  # Giữ lại 1000 mẫu từ tập huấn luyện
y_train = y_train[:1000]
x_test = x_test[:200]  # Giữ lại 200 mẫu từ tập kiểm tra
y_test = y_test[:200]

# Lưu dữ liệu vào thư mục cũ 
np.save(os.path.join(data_dir, 'x_train.npy'), x_train)
np.save(os.path.join(data_dir, 'y_train.npy'), y_train)
np.save(os.path.join(data_dir, 'x_test.npy'), x_test)
np.save(os.path.join(data_dir, 'y_test.npy'), y_test)

print("Dữ liệu MNIST sau khi giảm đã được lưu vào thư mục:", data_dir)

print("Số mẫu trong x_train ", x_train.shape[0]) #1000
print("Số mẫu trong x_test ", x_test.shape[0]) #200 