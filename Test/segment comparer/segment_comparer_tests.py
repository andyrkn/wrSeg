import areatests
import deviationtests
import color_range_tests
import background_color_tests

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
    0.04936015
]

missing_weights = [
    -0.13090575,
    -0.45466852,
    0.47876844,
    0.10216002,
]

extra_weights = [
    -0.00802379,
    -0.11083271,
    0.91855747,
    0.03785585
]
