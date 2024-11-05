""" Hàm tích chập chỉ dùng for đơn thuần """ 
def convolve_nest_loop(img, kernel):
    img_height = img.shape[0]
    img_width = img.shape[1]

    kernel_height = kernel.shape[0]
    kernel_width = kernel.shape[1]

    H = (kernel_height - 1) // 2
    W = (kernel_width - 1) // 2

    out = np.zeros((img_height, img_width))

    for i in np.arange(H, img_height - H):
        for j in np.arange(W, img_width - W):
            sum = 0
            for k in np.arange(-H, H + 1):
                for l in np.arange(-W, W + 1):
                    a = img[i + k, j + l]
                    w = kernel[H + k, W + l]
                    sum += (w * a)
            out[i, j] = sum
    return out

""" Hàm tích chập sử dụng numpy """
def convolve_np(img, kernel):
    img_height = img.shape[0]
    img_width = img.shape[1]

    kernel_height = kernel.shape[0]
    kernel_width = kernel.shape[1]

    H = (kernel_height - 1) // 2
    W = (kernel_width - 1) // 2

    out = np.zeros((img_height, img_width))

    for i in np.arange(H, img_height - H):
        for j in np.arange(W, img_width - W):
            for i in np.arange(H, img_height - H):
                for j in np.arange(W, img_width - W):
                    out[i - H, j - W] = np.tensordot(img[i - H:i + H + 1, j - W:j + W + 1], kernel, axes=((0, 1), (0, 1)))
    return out
""" Hàm tích chập sử dụng numpy + Bỏ viền giá trị 0 của đầu ra """
def convolve_np2(img, kernel):
    img_height = img.shape[0]
    img_width = img.shape[1]

    kernel_height = kernel.shape[0]
    kernel_width = kernel.shape[1]

    H = (kernel_height - 1) // 2
    W = (kernel_width - 1) // 2

    # Loại bỏ viền zero ở đây
    out = np.zeros((img_height - H * 2, img_width - W * 2))

    for i in np.arange(H, img_height - H):
        for j in np.arange(W, img_width - W):
            out[i - H, j - W] = np.tensordot(img[i - H:i + H + 1, j - W:j + W + 1], kernel, axes=((0, 1), (0, 1)))
    return out

import numpy as np

in_img = np.array([[1, 0, 0, 1, 0],
                   [0, 1, 1, 0, 1],
                   [1, 0, 1, 0, 1],
                   [1, 0, 0, 1, 1],
                   [0, 1, 1, 0, 1]
                   ])
kernel = np.array([[1, 0, 0],
                   [0, 1, 1],
                   [1, 0, 1]])
out_img = convolve_np4(in_img, kernel)
with np.printoptions(suppress=True):
    print(out_img)


