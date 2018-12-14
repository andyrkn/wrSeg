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
    sorted_scores = list(sorted(scores.items(), key=lambda x : x[1]))
    for key, value in sorted_scores:
        print("{}:  {}".format(key, value))
    return sorted_scores[0][1], sorted_scores[-1][1]

def test_category_weights(folder_path, left, right, output_file=None):
    weights_combinations =  set()
    weigth_range = [x / 10 for x in range(left, right)]
    for x in weigth_range:
        for y in weigth_range:
            for z in weigth_range:
                weights_combinations.add((x / (x + y + z), y / (x + y + z), z / (x + y + z)))

    big_string = ""

    for item in weights_combinations:
        segment_compare_score.common_score_weight = item[0]
        segment_compare_score.missing_score_weight = item[1]
        segment_compare_score.extra_score_weight = item[2]
        positive_score = test_folder(os.path.join(folder_path, "positive"))
        negative_score = test_folder(os.path.join(folder_path, "negative"))

        string = "{}\n{}\n{}\n\n".format(item, positive_score, negative_score)
        big_string += string
        print(string)
        
    if output_file:
        fd = open(output_file, "w")
        fd.write(big_string)
        fd.close()

if __name__ == "__main__":
    #test_category_weights(tests_path, 3, 4, "testresults38.txt")

    print("positive:")
    test_folder(os.path.join(tests_path, "positive"))
    print("\nnegative:")
    test_folder(os.path.join(tests_path, "negative"))