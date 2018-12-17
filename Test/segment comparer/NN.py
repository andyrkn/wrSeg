import os
import cv2

import segment
import segment_comparer_tests

import keras
import numpy as np

def get_inputs_from_folder(folder_path):
    all_inputs = []
    paths = []

    for test_name in os.listdir(folder_path):
        test_path = os.path.join(folder_path, test_name)
        if os.path.isdir(test_path):
            original_path = os.path.join(test_path, "original.png")
            original_image = cv2.imread(original_path)
            for subtest_name in os.listdir(test_path):
                subtest_path = os.path.join(test_path, subtest_name)
                if os.path.isdir(subtest_path):
                    output_path = os.path.join(subtest_path, "output.png")
                    target_path = os.path.join(subtest_path, "target.png")
                    
                    output_image = cv2.imread(output_path)
                    target_image = cv2.imread(target_path)
                    output_segment = segment.get_segment_info_from_images(original_image, output_image)
                    target_segment = segment.get_segment_info_from_images(original_image, target_image)

                    common = segment.get_intersection_segment_info(output_segment, target_segment)
                    missing = segment.get_minus_segments_info(target_segment, output_segment)
                    extra = segment.get_minus_segments_info(output_segment, target_segment)

                    common_scores = [test(common, target_segment) if common else 0 for test in segment_comparer_tests.common_area_tests] 
                    missing_scores = [test(missing, target_segment) if any(missing) else 1 for test in segment_comparer_tests.missing_area_tests]
                    extra_scores = [test(extra, output_segment) if any(extra) else 1 for test in segment_comparer_tests.extra_area_tests]

                    subtest_inputs = common_scores + missing_scores + extra_scores
                    all_inputs += [subtest_inputs]
                    paths += [subtest_path]
    return all_inputs, paths

tests_path = "./tests"

if __name__ == "__main__":
    positive_inputs = get_inputs_from_folder(os.path.join(tests_path, "positive"))
    negative_inputs = get_inputs_from_folder(os.path.join(tests_path, "negative"))

    
    all_inputs = np.array(positive_inputs[0] + negative_inputs[0])
    all_inputs_names = positive_inputs[1] + negative_inputs[1]
    all_outputs = [1 if "positive" in name else 0 for name in all_inputs_names]

    print(all_outputs)

    nncomparer = keras.Sequential()
    nncomparer.add(keras.layers.InputLayer((9,)))
    nncomparer.add(keras.layers.Dropout(0.3))
    nncomparer.add(keras.layers.Dense(1, activation=keras.activations.linear))
    nncomparer.compile(
        loss=keras.losses.mean_squared_error,
        optimizer=keras.optimizers.SGD(lr=0.1),
        metrics=['accuracy']
        )

    history = nncomparer.fit(all_inputs, all_outputs, epochs=60, verbose=False)
    loss, acc = nncomparer.evaluate(all_inputs, all_outputs, verbose=False)
    print(acc)

    # #print(nncomparer.layers[0].get_weights()[0])
    # #print(nncomparer.layers[0].get_weights()[1])

    for input_set, name in zip(all_inputs, all_inputs_names):
        print(name)
        print(nncomparer.predict(input_set.reshape(-1, 9), batch_size=1))

