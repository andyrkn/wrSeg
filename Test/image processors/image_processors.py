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

def pixalate(image, strength=3):
    new_image = image.copy()
    for i in range(0, new_image.shape[0]):
        for j in range(0, new_image.shape[1]):
            new_image[i][j] = new_image[(i // strength) * strength][(j // strength) * strength]
    return new_image