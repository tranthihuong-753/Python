import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist

# Tạo thư mục để lưu trữ dữ liệu
data_dir = 'D:\CMC_Ky4\CODE\Python\cmc\chuong4_CNN\PhanLoaiSoVoiMNIST\data' # Đường dẫn lưu tập dữ liệu 
os.makedirs(data_dir, exist_ok=True)

# Tải dữ liệu MNIST
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Lưu dữ liệu vào thư mục
np.save(os.path.join(data_dir, 'x_train.npy'), x_train)
np.save(os.path.join(data_dir, 'y_train.npy'), y_train)
np.save(os.path.join(data_dir, 'x_test.npy'), x_test)
np.save(os.path.join(data_dir, 'y_test.npy'), y_test)

print("Dữ liệu MNIST đã được lưu vào thư mục:", data_dir)
