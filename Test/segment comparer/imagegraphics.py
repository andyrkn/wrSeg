import numpy as np
import cv2

def draw_highlight_rectangle(image, top_left, bot_right, highlight_color, border_color, border_thickness=1, reversed=False):
    if len(image.shape) == 3:
        new_image = image.copy()
    else:
        new_image = np.zeros((image.shape[0], image.shape[1], 3))
        for x in range(new_image.shape[0]):
            for y in range(new_image.shape[1]):
                new_image[x][y] = image[x][y]

    if reversed:
        for x in range(new_image.shape[0]):
            for y in range(new_image.shape[1]):
                if (top_left[1] > x or x > bot_right[1]) or (top_left[0] > y or y > bot_right[0]):
                    new_image[x][y] = ((new_image[x][y] / 255) * (highlight_color) / 255) * 255
    else:
        for x in range(top_left[0], bot_right[0]):
            for y in range(top_left[1], bot_right[1]):
                new_image[y][x] = ((new_image[y][x] / 255) * (np.array(highlight_color) / 255)) * 255
    cv2.rectangle(new_image, top_left, bot_right, border_color, border_thickness)
    return new_image

""" 
    original_image - a copy of this image will be created, drawn upon and then returned
    segment_info_1, segment_info_2 - two SegmentInfo with the coordinates of the rectangles
    color_1, color_2 - border colors
    fill_color_1, fill_color_2 - fill colors
    border_thickness - border thickness of both rectangles
    return - a copy of original_image (numpy array)
"""
def create_debug_image(original_image, segment_info_1, segment_info_2, color_1, color_2, fill_color_1, fill_color_2, border_thickness=1):
    new_image = original_image.copy()
    new_image = draw_highlight_rectangle(new_image, segment_info_1.top_left, segment_info_1.bot_right, color_1, fill_color_1, border_thickness)
    new_image = draw_highlight_rectangle(new_image, segment_info_2.top_left, segment_info_2.bot_right, color_2, fill_color_2, border_thickness)
    return new_image
