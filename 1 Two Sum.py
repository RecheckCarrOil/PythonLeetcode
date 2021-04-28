from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        viable_indices = []
        for num in nums:
            if (num <= target and target >= 0) or (num >= target and target < 0):
                viable_indices.append(nums.index(num))
        for ind in viable_indices:
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

