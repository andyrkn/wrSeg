import segment
import areatests
import deviationtests
import cv2

common_score_weight = 0.4
missing_score_weight = 0.3
extra_score_weight = 0.3

def score(output, target):
    comparer = segment.SegmentComparer()

    comparer.set_category_weights(common_score_weight, missing_score_weight, extra_score_weight)

    # test for how much area the target and output have in common
    comparer.add_common_area_test(areatests.common_area_percentage, 0.5)
    # tests for the percentage of the difference area between target and output
    comparer.add_missing_area_test(areatests.uncommon_area_percentage_segments, 0.3)
    comparer.add_extra_area_test(areatests.uncommon_area_percentage_segments, 0.3)

    # tests for uniformity (0 - if it is only background, 1 - if it might contain info)
    comparer.add_missing_area_test(deviationtests.uniformity_segments, 0.7)
    comparer.add_extra_area_test(deviationtests.uniformity_segments, 0.7)

    result = comparer.compare(output, target)

    # print(result.common_area_scores)
    # print(result.missing_area_scores)
    # print(result.extra_area_scores)
    return result.total_score

def score_from_images(original_image, output_image, target_image):
    output = segment.get_segment_info_from_images(original_image, output_image)
    target = segment.get_segment_info_from_images(original_image, target_image)
    return score(output, target)

def score_from_paths(original_path, output_path, target_path):
    original_image = cv2.imread(original_path, cv2.IMREAD_COLOR)
    output_image = cv2.imread(output_path, cv2.IMREAD_COLOR)
    target_image = cv2.imread(target_path, cv2.IMREAD_COLOR)
    return score_from_images(original_image, output_image, target_image)
