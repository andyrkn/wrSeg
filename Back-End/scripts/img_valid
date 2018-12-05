#!/usr/bin/env python

from PIL import Image
import os.path
def valid_img(filename):
    min_width = 600
    min_height = 600
    max_width = 10000
    max_height = 10000

    if not os.path.isfile(filename):
        return False
    im = Image.open(filename)

    # if im.format != "PNG":
    #     return False

    width, height = im.size
    if width < min_width or height < min_height:
        return False
    #if width > max_width or height > max_height:
    #   resize

    return True
