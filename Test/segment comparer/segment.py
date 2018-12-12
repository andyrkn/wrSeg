import cv2
import numpy as np

class SegmentInfo:
    def __init__(self, original_image, position, width, height):
        self.original_image = original_image
        self.position = position
        self.width = width
        self.height = height

        self.image = original_image[self.top_left[1]:self.bot_right[1], self.top_left[0]:self.bot_right[0]]

    @property
    def top_left(self):
        return self.position

    @property
    def bot_right(self):
        return (self.position[0] + self.width, self.position[1] + self.height)

    @property 
    def top_right(self):
        return (self.position[0] + self.width, self.position[1])

    @property 
    def bot_left(self):
        return (self.position[0], self.position[1] + self.height)

    @property
    def area(self):
        return self.width * self.height

"""  Each field will be a number in [0, 1] """
class SegmentComparerResult:
    def __init__(self, common_area_scores, missing_area_scores, extra_area_scores, total_score):
        self.common_area_scores = common_area_scores
        self.missing_area_scores = missing_area_scores
        self.extra_area_scores = extra_area_scores
        self.total_score = total_score

""" 
    This class has 3 fields for tests, each a list of function with 2 arguments
    and returning a score in interval [0, 1] (0 - bad score, 1 - good score)

    common_area_tests - tests for the intersection of the output and the target
        param1: SegmentInfo of intersection segment
        param2: SegmentInfo of target segment

    missing_area_tests - tests for the area in target, but not in output
        param1: a list of 4 SegmentInfos [top, bot, left, right]
                 for the segments in target, but not in output
        param2: SegmentInfo of target segment

    extra_area_tests - tests for the area in output, but not in target
        param1: a list of 4 SegmentInfos [top, bot, left, right]
                for the segments in output, but not in target
        param2: SegmentInfo of output segment

    Each category of tests has a weight associated used in computing the total score
    The weights for each test will be normalized automatically
"""
class SegmentComparer:
    def __init__(self):
        self.common_area_tests = []
        self.missing_area_tests = []
        self.extra_area_tests = []

        self.common_weights = []
        self.missing_weights = []
        self.extra_weights = []

        self.common_weights_sum = 0
        self.missing_weights_sum = 0
        self.extra_weights_sum = 0

        self.common_score_weight = 0.34
        self.missing_score_weight = 0.33
        self.extra_score_weight = 0.33

    """
        param1: SegmentInfo of output segment
        param2: SegemntInfo of target segment
        return: a SegmentCompareResult with the resulting score
    """
    def compare(self, output, target):
        common_area_score = self.common_area_score(output, target)
        missing_area_score = self.missing_area_score(output, target)
        extra_area_score = self.extra_area_score(output, target)

        total_score = (common_area_score * self.common_score_weight +
                       missing_area_score * self.missing_score_weight +
                       extra_area_score * self.extra_score_weight)

        return SegmentComparerResult(common_area_score, missing_area_score, extra_area_score, total_score)

    def add_common_area_test(self, test, weight=1):
        self.common_area_tests.append(test)
        self.common_weights.append(weight)
        self.common_weights_sum += weight

    def add_missing_area_test(self, test, weight=1):
        self.missing_area_tests.append(test)
        self.missing_weights.append(weight)
        self.missing_weights_sum += weight

    def add_extra_area_test(self, test, weight=1):
        self.extra_area_tests.append(test)
        self.extra_weights.append(weight)
        self.extra_weights_sum += weight

    def common_area_score(self, output, target):
        common = get_intersection_segment_info(output, target)
        if common:
            total_score = 0
            common_area_scores = [test(common, target) for test in self.common_area_tests]
            for i, score in enumerate(common_area_scores):
                total_score += score * self.common_weights[i] / self.common_weights_sum
            return total_score
        else:
            return 1

    def missing_area_score(self, output, target):
        missing = get_minus_segments_info(target, output)
        if any(missing):
            total_score = 0
            missing_area_scores = [test(missing, target) for test in self.missing_area_tests]
            for i, score in enumerate(missing_area_scores):
                total_score += score * self.missing_weights[i] / self.missing_weights_sum
            return total_score
        else:
            return 1

    def extra_area_score(self, output, target):
        extra = get_minus_segments_info(output, target)
        if any(extra):
            total_score = 0
            extra_area_scores = [test(extra, output) for test in self.extra_area_tests]
            for i, score in enumerate(extra_area_scores):
                total_score += score * self.extra_weights[i] / self.extra_weights_sum
            return total_score
        else:
            return 1

    def set_category_weights(self, common_score_weight, missing_score_weight, extra_score_weight):
        self.common_score_weight = common_score_weight
        self.missing_score_weight = missing_score_weight
        self.extra_score_weight = extra_score_weight
        weights_sum = common_score_weight + missing_score_weight + extra_score_weight 
        self.common_score_weight /= weights_sum
        self.missing_score_weight /= weights_sum
        self.extra_score_weight /= weights_sum

""" Return a SegmentInfo created from an image """
def get_segment_info_from_images(original_image, segment_image):
    match_result = cv2.matchTemplate(original_image, segment_image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(match_result)
    return SegmentInfo(original_image, max_loc, segment_image.shape[1], segment_image.shape[0])

""" Return - a SegmentInfo with information about the common are of segment_info_1 and segment_info_2,
           - None if there is no intersection """
def get_intersection_segment_info(segment_info_1, segment_info_2):
    intersection_bot = min(segment_info_1.bot_right[1], segment_info_2.bot_right[1])
    intersection_top = max(segment_info_1.top_left[1], segment_info_2.top_left[1])
    intersection_right = min(segment_info_1.bot_right[0], segment_info_2.bot_right[0])
    intersection_left = max(segment_info_1.top_left[0], segment_info_2.top_left[0])
    intersection_width = intersection_right - intersection_left
    intersection_height = intersection_bot - intersection_top

    if intersection_width > 0 and intersection_height > 0:
        intersection = SegmentInfo(segment_info_1.original_image, (intersection_left, intersection_top), intersection_width, intersection_height)
        return intersection
    else:
        return None

""" Return a list of SegmentInfo in this order [top, bot, left, right],
 if a segment has no area None will be added to the list in its place"""
def get_minus_segments_info(segment_info_1, segment_info_2):
    common = get_intersection_segment_info(segment_info_1, segment_info_2)

    # top segment
    top_segment = None
    if segment_info_1.top_left[1] < segment_info_2.top_left[1]:
        top_left = segment_info_1.top_left
        width = segment_info_1.width
        height = segment_info_2.top_left[1] - segment_info_1.top_left[1]
        top_segment = SegmentInfo(segment_info_1.original_image, top_left, width, height)

    # bot segment
    bot_segment = None
    if segment_info_1.bot_right[1] > segment_info_2.bot_right[1]:
        top_left = (segment_info_1.top_left[0], segment_info_2.bot_right[1]) 
        width = segment_info_1.width
        height = segment_info_1.bot_right[1] - segment_info_2.bot_right[1]
        bot_segment = SegmentInfo(segment_info_1.original_image, top_left, width, height)
    
    if common:
        is_common_top_inside = segment_info_1.top_left[1] <= common.top_left[1] <= segment_info_1.bot_right[1]
        is_common_bot_inside = segment_info_1.top_left[1] <= common.bot_right[1] <= segment_info_1.bot_right[1]
    else:
        is_common_top_inside = False
        is_common_bot_inside = False

    # left segment
    left_segment = None
    if is_common_top_inside and segment_info_1.top_left[0] < segment_info_2.top_left[0]:
        top_left = (segment_info_1.top_left[0], common.top_left[1])
        width = segment_info_2.top_left[0] - segment_info_1.top_left[0]
        height = common.width
        left_segment = SegmentInfo(segment_info_1.original_image, top_left, width, height)

    # right segment
    right_segment = None
    if is_common_bot_inside and segment_info_1.bot_right[0] > segment_info_2.bot_right[0]:
        top_left = (segment_info_2.bot_right[0], common.top_left[1])
        width = segment_info_1.bot_right[0] - segment_info_2.bot_right[0]
        height = common.height
        right_segment = SegmentInfo(segment_info_1.original_image, top_left, width, height)

    return [top_segment, bot_segment, left_segment, right_segment]
