def common_area_percentage(small_image_info, big_image_info):
    return small_image_info.area / big_image_info.area

def common_area_percentage_segments(small_image_segments, big_image_info):
    area_sum = 0
    for segment in small_image_segments:
        if segment:
            area_sum += segment.area
    return area_sum / big_image_info.area

def uncommon_area_percentage(small_image_info, big_image_info):
    return 1 - common_area_percentage(small_image_info, big_image_info)

def uncommon_area_percentage_segments(small_image_segments, big_image_info):
    return 1 - common_area_percentage_segments(small_image_segments, big_image_info)