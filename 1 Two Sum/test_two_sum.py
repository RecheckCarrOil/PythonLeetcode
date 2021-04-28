import pytest
from two_sum import *


@pytest.mark.parametrize("input_list, target, result",
                         [([2, 7, 11, 15], 9, [0, 1]), ([3, 2, 4], 6, [1, 2]), ([3, 3], 6, [0, 1])])
def test_twoSum(input_list, target, result):
    assert Solution.twoSum(input_list, target) == result
