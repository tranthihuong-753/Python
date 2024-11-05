import os
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

#1. Tải tập dữ liệu CIFAR-10
# Đường dẫn đến thư mục chứa dữ liệu
path = 'D:\CMC_Ky4\CODE\Python\cmc\chuong4_CNN\PhanLoaiAnh\data'

# Tải dữ liệu từ các file đã lưu
x_train = np.load(os.path.join(path, 'x_train.npy'))
y_train = np.load(os.path.join(path, 'y_train.npy'))
x_test = np.load(os.path.join(path, 'x_test.npy'))
y_test = np.load(os.path.join(path, 'y_test.npy'))

#2. Chuẩn hóa dữ liệu
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

# Định nghĩa các lớp
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

model = Sequential()

# Thêm các lớp
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

# Biên dịch mô hình
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Huấn luyện mô hình
model.fit(x_train, y_train, epochs=10, batch_size=64, validation_data=(x_test, y_test))

print("Huấn luyện xong")
print("Thử nghiệm hiệu quả mô hình")
# Đánh giá mô hình trên tập kiểm tra
# Đánh giá mô hình trên tập kiểm tra
test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=0)
print(f"Độ mất mát trên tập kiểm tra: {test_loss}")
print(f"Độ chính xác trên tập kiểm tra: {test_accuracy}")

# Thực hiện dự đoán trên tập kiểm tra
predictions = model.predict(x_test)

# Kiểm tra kết quả dự đoán cho 5 mẫu đầu tiên
for i in range(5):
    plt.imshow(x_test[i])  # CIFAR-10 ảnh màu RGB 32x32
    plt.title(f"Dự đoán: {np.argmax(predictions[i])} - Nhãn thật: {y_test[i][0]}")
    plt.axis('off')  # Tắt trục tọa độ cho ảnh
    plt.show()