from typing import List


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        other_halves = {}
        for i, num in enumerate(nums):
            if num in other_halves:
                return [other_halves[num], i]
            other_halves[target - num] = i
