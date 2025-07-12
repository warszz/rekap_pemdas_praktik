import numpy as np
from scipy.signal import convolve2d

# Simple 2D array
image = np.array([[1, 2], [3, 4]], dtype=np.float64)

# Simple kernel
kernel = np.array([[1, 0], [0, -1]], dtype=np.float64)

# Convolution
result = convolve2d(image, kernel, mode='same', boundary='fill', fillvalue=0)

print("Result of Convolution:")
print(result)


# Define the image as a 2D NumPy array
image = np.array([
    [100, 120, 130],
    [110, 115, 125],
    [105, 110, 120]
], dtype=np.float64)

# Define the blur kernel
blur_kernel = np.ones((3, 3), dtype=np.float64) / 9

# Define the edge detection kernel (Sobel)
edge_kernel = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
], dtype=np.float64)

# Convolve with blur kernel, keep same size, pad edges with zeros
blur_result = convolve2d(image, blur_kernel, mode='same', boundary='fill', fillvalue=0)

# Convolve with edge detection kernel (Sobel), keep same size, pad edges with zeros
edge_result = convolve2d(image, edge_kernel, mode='same', boundary='fill', fillvalue=0)

# Print the results
print("Hasil Blur:")
print(blur_result)
print("Hasil Edge Detection:")
print(edge_result)

