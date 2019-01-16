import numpy as np
import cv2

def tightness(small_image_info, big_image_info):
    if len(small_image_info.image.shape) == 3 and small_image_info.image.shape[2] == 3:
        gray_image = cv2.cvtColor(small_image_info.image, cv2.COLOR_BGR2GRAY)
    else:
        gray_image = small_image_info.image

    return gray_image.min() / gray_image.max()

def tightness_segments(small_image_segments, big_image_info):
    min_pixel = 255
    max_pixel = 0
    for segment in small_image_segments:
        if segment:
            if len(segment.image.shape) == 3 and segment.image.shape[2] == 3:
                gray_image = cv2.cvtColor(segment.image, cv2.COLOR_BGR2GRAY)
            else:
                gray_image = segment.image

            if gray_image.min() < min_pixel:
                min_pixel = gray_image.min()
            if gray_image.max() > max_pixel:
                max_pixel = gray_image.max()

    return min_pixel / max_pixel

def spreadness(small_image_info, big_image_info):
    return 1 - tightness(small_image_info, big_image_info)

def spreadness_segments(small_image_segments, big_image_info):
    return 1 - tightness_segments(small_image_segments, big_image_info)


# import segment

# img = cv2.imread(r".\testimg.bmp", cv2.IMREAD_COLOR)

# print(tightness(segment.SegmentInfo(img, (0, 0), img.shape[1], img.shape[0]), None))