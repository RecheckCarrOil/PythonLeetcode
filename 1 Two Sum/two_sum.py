from typing import List


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        for ind in range(len(nums)):
            nums_copy = nums.copy()
            nums_copy.pop(ind)
            for num in nums_copy:
                if nums[ind] + num == target:
                    return [ind, nums.index(num, ind+1)]


if __name__ == "__main__":
    instance = Solution()
    nums = [-1,-2,-3,-4,-5]
    target = -8
    result = instance.twoSum(nums, target)

    print(result)

