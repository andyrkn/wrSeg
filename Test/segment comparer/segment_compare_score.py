import segment
import segment_comparer_tests
import cv2

comparer = segment.SegmentComparer()

for i, test in enumerate(segment_comparer_tests.common_area_tests):
    comparer.add_common_area_test(test, segment_comparer_tests.common_weights[i])
for i, test in enumerate(segment_comparer_tests.missing_area_tests):
    comparer.add_missing_area_test(test, segment_comparer_tests.missing_weights[i])
for i, test in enumerate(segment_comparer_tests.extra_area_tests):
    comparer.add_extra_area_test(test, segment_comparer_tests.extra_weights[i])

def score(output, target, all_scores=False):
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
