from segment_score_functions import areatests
from segment_score_functions import deviationtests
from segment_score_functions import color_range_tests
from segment_score_functions import background_color_tests

common_area_tests = [
    areatests.common_area_percentage
]

missing_area_tests = [ 
    areatests.uncommon_area_percentage_segments,
    deviationtests.uniformity_segments,
    color_range_tests.tightness_segments,
    background_color_tests.whiteness_segments
]

extra_area_tests = missing_area_tests

common_weights = [
    0.5
]

missing_weights = [
    0.2,
    0.125,
    0.1,
    0.075
]

extra_weights = [
    0.05,
    0.15,
    0.15,
    0.05
]
