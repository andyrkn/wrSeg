import segment_compare_score
import os

tests_path = "./tests"

def test_folder(folder_path):
    scores = dict()
    for test_name in os.listdir(folder_path):
        test_path = os.path.join(folder_path, test_name)
        if os.path.isdir(test_path):
            original_path = os.path.join(test_path, "original.png")
            output_path = os.path.join(test_path, "output.png")
            target_path = os.path.join(test_path, "target.png")
            score = segment_compare_score.score_from_paths(original_path, output_path, target_path)
            scores[test_name] = score
    for key, value in sorted(scores.items(), key=lambda x : x[1]):
        print("{}:  {}".format(key, value))

if __name__ == "__main__":
    print("positive:")
    test_folder(os.path.join(tests_path, "positive"))
    print("negative:")
    test_folder(os.path.join(tests_path, "negative"))
