import segment_compare_score
import os

import cv2
import segment
import segment_comparer_tests

tests_path = "./tests"

def test_folder(folder_path):
    scores = dict()
    for test_name in os.listdir(folder_path):
        test_path = os.path.join(folder_path, test_name)
        if os.path.isdir(test_path):
            original_path = os.path.join(test_path, "original.png")
            for subtest_name in os.listdir(test_path):
                subtest_path = os.path.join(test_path, subtest_name)
                if os.path.isdir(subtest_path):
                    output_path = os.path.join(subtest_path, "output.png")
                    target_path = os.path.join(subtest_path, "target.png")
                    score = segment_compare_score.score_from_paths(original_path, output_path, target_path)
                    scores[test_name + "  " + subtest_name] = score
    sorted_scores = list(sorted(scores.items(), key=lambda x : x[1]))
    for key, value in sorted_scores:
        print("{}:  {}".format(key, value))
    return sorted_scores[0][1], sorted_scores[-1][1]
   

if __name__ == "__main__":
    print("positive:")
    test_folder(os.path.join(tests_path, "positive"))
    print("\nnegative:")
    test_folder(os.path.join(tests_path, "negative"))
