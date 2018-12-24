import numpy as np
import cv2

def whiteness(small_image_info, big_image_info):
    if len(small_image_info.image.shape) == 3 and small_image_info.image.shape[2] == 3:
        gray_image = cv2.cvtColor(small_image_info.image, cv2.COLOR_BGR2GRAY)
    else:
        gray_image = small_image_info.image

    return 1 - np.mean(gray_image) / 255

def whiteness_segments(small_image_segments, big_image_info):
    gray_images = []
    for segment in small_image_segments:
        if segment:
            if len(segment.image.shape) == 3 and segment.image.shape[2] == 3:
                gray_images += [cv2.cvtColor(segment.image, cv2.COLOR_BGR2GRAY)]
            else:
                gray_images += [segment.image]

    pixels = np.array([0])
    for gray_image in gray_images:
            pixels = np.concatenate((pixels, gray_image.flatten()))
    pixels = np.delete(pixels, 0)

    return 1 - np.mean(pixels) / 255