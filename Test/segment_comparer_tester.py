import segment_comparer
import os

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
                    score = segment_comparer.score_from_paths(original_path, output_path, target_path)
                    scores[test_name + "  " + subtest_name] = score
    return sorted(scores.items(), key=lambda x : x[1])

def print_scores(scores_dict):
    for key, value in scores_dict:
        print("{}:  {}".format(key, value))
   
if __name__ == "__main__":
    print("positive:")
    print_scores(test_folder(os.path.join(tests_path, "positive")))
    print("\nnegative:")
    print_scores(test_folder(os.path.join(tests_path, "negative")))
