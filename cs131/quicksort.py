# coding: utf-8

import numpy as np
from scipy.misc import imread, imsave, imresize
from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[int(len(arr) / 2)]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


# print(quicksort([3, 6, 1, 23, 66, 0, -1]))
#
#
# def fibonacci(n):
#     if n <= 1:
#         return 1
#     return fibonacci(n - 2) + fibonacci(n - 1)
#
#
# for i in range(20):
#     print(fibonacci(i), end=' ')


a = np.array([[1, 2], [3, 4], [5, 6]])
bool_idx = (a > 2)
print(type(bool_idx))
print(bool_idx)
print(a[bool_idx])

x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)

print(x + y)
print(np.add(x, y))

print(x - y)
print(np.subtract(x, y))

print(x * y)
print(np.multiply(x, y))

print(x / y)
print(np.divide(x, y))

print(np.sqrt(x))

x = np.array([1, 2, 3])
y = np.array([1, 2])
print(x.shape)

img = imread('../stanford-tensorflow-tutorials/data/friday.jpg')
print(img.dtype, img.shape)
img_tinted = img * [1, 0.95, 0.7]
img_tinted = imresize(img_tinted, (300, 300))
imsave('tinted.jpg', img_tinted)

x = np.array([[0, 1], [1, 0], [2, 0]])
print(x)

d = squareform(pdist(x, 'euclidean'))
print(d)

x = np.arange(0, 2 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Sine and Cosine')
plt.legend(['Sine', 'Cosine'])
plt.subplot(2, 1, 1)
plt.plot(x, y_sin)
plt.title('Sine')
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('Cosine')
plt.show()

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.subplot(1, 2, 2)
plt.imshow(np.uint8(img_tinted))
plt.show()
