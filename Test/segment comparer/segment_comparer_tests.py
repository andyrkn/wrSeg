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