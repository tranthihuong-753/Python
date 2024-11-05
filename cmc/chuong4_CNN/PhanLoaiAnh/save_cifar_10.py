import os 
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import cifar10 

path = 'D:\CMC_Ky4\CODE\Python\cmc\chuong4_CNN\PhanLoaiAnh\data'
os.makedirs(path, exist_ok=True)

(x_train, y_train), (x_test, y_test) = cifar10.load_data()

np.save(os.path.join(path, 'x_train.npy'), x_train)
np.save(os.path.join(path, 'y_train.npy'), y_train)
np.save(os.path.join(path, 'x_test.npy'), x_test)
np.save(os.path.join(path, 'y_test.npy'), y_test)

print("Data saved")