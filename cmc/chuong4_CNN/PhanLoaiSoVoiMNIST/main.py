import os
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

# 1. Tải dữ liệu x_train, y_train, x_test, y_test 
# Đường dẫn đến thư mục chứa dữ liệu
data_dir = 'D:\CMC_Ky4\CODE\Python\cmc\chuong4_CNN\PhanLoaiSoVoiMNIST\data'

# Tải dữ liệu từ các file đã lưu
x_train = np.load(os.path.join(data_dir, 'x_train.npy'))
y_train = np.load(os.path.join(data_dir, 'y_train.npy'))
x_test = np.load(os.path.join(data_dir, 'x_test.npy'))
y_test = np.load(os.path.join(data_dir, 'y_test.npy'))

# 2. Chuẩn hóa dữ liệu
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

# Thêm chiều cho dữ liệu để phù hợp với đầu vào của mô hình
    # reshape() -> Thay đổi kích thước mảng + Không làm thay đổi nội dung 
    # x_tran mới là 1 ma trận với số lượng không đổi x_train.shape[0] = 1000 
    # kích thước mỗi phần tử là 28x28 , 1 kênh màu 
x_train = x_train.reshape((x_train.shape[0], 28, 28, 1))
x_test = x_test.reshape((x_test.shape[0], 28, 28, 1))

# Định nghĩa các lớp (MNIST có 10 lớp: số 0 đến 9)
class_names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# Tạo mô hình tuần tự để xếp chồng các lớp, với đầu ra của lớp này là đầu vòa của lớp sau  
model = Sequential()

#Thêm các lớp
# Lớp tích chập 2 chiều : 
    # Conv2D(32, (3, 3) lớp tích chập 2 chiều có 32 bộ lọc , kích thước 3x3 , số kênh = số kênh của ma trận điểm ảnh = 3 (Luôn 1 mẫu -> 1 ma trận 1 kênh)
    # Input : 28 28 1 -> ma trận điểm ảnh kích thước 28x28 , có 1 kênh   
    # Output: 26 26 32 -> -> ma trận điểm ảnh kích thước 26x26 , có 32 kênh    
        # (28, 28)*(3, 3) = (26, 26) ?28 - 3 + 1 = 26?
        # ma trận điểm ảnh có 1 kênh, đi qua 32 bộ lọc , đầu ra là mẫu có 32 kênh 
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1))) 

# Lớp Max-pooling 
    # Dùng ma trận kích thước 2x2 trượt trên ma trận điểm ảnh để tìm max, với bước nhảy strate = 2 
    # Input : 26 26 32 -> -> ma trận điểm ảnh kích thước 26x26 , có 32 kênh  
    # Output: 13 13 32 
model.add(MaxPooling2D(pool_size=(2, 2)))
# Lớp tích chập 2 chiều : 
    # Input : 13 13 32  
    # Output: 11 11 64
model.add(Conv2D(64, (3, 3), activation='relu'))
# Lớp Max-pooling 
    # Input : 11 11 64 
    # Output: 5 5 64 
model.add(MaxPooling2D(pool_size=(2, 2)))
# Lớp Flatten() 
    # Output là một mảng 1D 
model.add(Flatten())
# Lớp Dense 
    # Lớp kết nối đầy đủ (fully connected layers).
    # 128 noron 
model.add(Dense(128, activation='relu'))
# Lớp Dropout 
    # Ngăn ngừa hiện tượng overfitting. 
    # Trong mỗi lần huấn luyện, nó sẽ "bỏ qua" 50% số noron một cách ngẫu nhiên.
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

model.summary() # in ra KT output, para dưới dạng bảng 

# Biên dịch mô hình (create)
    # thuật toán tối ưu hóa (optimizer) để tối ưu trọng số.
    # Hàm mất mát (loss)
    # Phép đo đánh giá hiệu suất (metrics).
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Huấn luyện mô hình
    # epochs chỉ số lần lặp lại quá trình huấn luyện qua toàn bộ tập dữ liệu. 
    # Ở đây, mô hình sẽ lặp qua toàn bộ x_train và y_train 10 lần để tối ưu hóa các trọng số.
    # batch_size là số lượng mẫu mà mô hình xử lý trước khi cập nhật trọng số.
    # Ở đây, 64 mẫu sẽ được xử lý cùng lúc (một batch), sau đó mô hình sẽ điều chỉnh trọng số dựa trên lỗi trung bình của 64 mẫu đó.
model.fit(x_train, y_train, epochs=10, batch_size=64, validation_data=(x_test, y_test))

# TEST 
# Đánh giá mô hình trên tập kiểm tra
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print(f"Độ mất mát trên tập kiểm tra: {test_loss}")
print(f"Độ chính xác trên tập kiểm tra: {test_accuracy}")
# Thực hiện dự đoán trên tập kiểm tra
predictions = model.predict(x_test)
# Kiểm tra kết quả dự đoán cho 5 mẫu đầu tiên
for i in range(5):
    plt.imshow(x_test[i].reshape(28, 28), cmap='gray')
    plt.title(f"Dự đoán: {np.argmax(predictions[i])} - Nhãn thật: {y_test[i]}")
    plt.show()



