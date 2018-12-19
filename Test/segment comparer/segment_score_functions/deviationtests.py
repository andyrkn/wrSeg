import numpy as np

def deviation(small_image_info, big_image_info):
    return np.std(small_image_info.image) / 127.5 

def uniformity(small_image_info, big_image_info):
    return 1 - deviation(small_image_info, big_image_info)

def deviation_segments(small_image_segments, big_image_info):
    pixels = np.array([0])
    for segment in small_image_segments:
        if segment:
            pixels = np.concatenate((pixels, np.array(segment.image).flatten()))
    pixels = np.delete(pixels, 0)
    return np.std(pixels) / 127.5

def uniformity_segments(small_image_segments, big_image_info):
    return 1 - deviation_segments(small_image_segments, big_image_info)
