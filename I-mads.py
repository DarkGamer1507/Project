import numpy as np
import matplotlib.pyplot as plt
import cv2

#apply gaussian blur to an image
def gaussian_blur(img, kernel_size):
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

#apply canny edge detection to an image
def canny(img, low_threshold, high_threshold):
    return cv2.Canny(img, low_threshold, high_threshold)

image=cv2.imread('try.jpg', cv2.IMREAD_GRAYSCALE)

gaussian_blur_img = gaussian_blur(image, 5)
canny_img = canny(gaussian_blur_img, 50, 150)

# Display images
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 3, 2)
plt.imshow(gaussian_blur_img, cmap='gray')
plt.title('Gaussian Blur Image')

plt.subplot(1, 3, 3)
plt.imshow(canny_img, cmap='gray')
plt.title('Canny Image')

plt.show()



