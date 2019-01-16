import cv2
import numpy

def invert_colors(image):
    return 255 - image

def blur(image, kernel_size):
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

def noise(image, strength=0.5):
    new_image = image.copy()
    means = (127, 127, 127)
    stds = (50, 50, 50)
    noise = cv2.randn(new_image, means, stds)
    return cv2.addWeighted(image, 1 - strength, new_image, strength, 0.0)