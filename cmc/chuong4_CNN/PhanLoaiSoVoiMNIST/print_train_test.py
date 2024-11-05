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

# In ra 3 mẫu từ tập huấn luyện
print("3 mẫu từ tập huấn luyện:")
for i in range(3):
    print("Hình ảnh:", x_train[i])  # In ra hình ảnh dưới dạng mảng
    print("Nhãn:", y_train[i])      # In ra nhãn tương ứng
    print()

# In ra 3 mẫu từ tập kiểm tra
print("3 mẫu từ tập kiểm tra:")
for i in range(3):
    print("Hình ảnh:", x_test[i])   # In ra hình ảnh dưới dạng mảng
    print("Nhãn:", y_test[i])       # In ra nhãn tương ứng
    print()

# Hiển thị 3 mẫu từ tập huấn luyện
plt.figure(figsize=(10, 4))
for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(x_train[i], cmap='gray')  # Hiển thị hình ảnh với màu xám
    plt.title(f'Nhãn: {y_train[i]}')
    plt.axis('off')
plt.show()

# Hiển thị 3 mẫu từ tập kiểm tra
plt.figure(figsize=(10, 4))
for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(x_test[i], cmap='gray')  # Hiển thị hình ảnh với màu xám
    plt.title(f'Nhãn: {y_test[i]}')
    plt.axis('off')
plt.show()