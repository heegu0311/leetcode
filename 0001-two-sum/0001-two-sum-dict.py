from typing import List


def twoSum_dictionary(nums: List[int], target: int) -> List[int]:
    memo = {}
    for i, num in enumerate(nums):
        needed = target - num
        if needed in memo:
            return [memo[needed], i]
        memo[num] = i


print(twoSum_dictionary([4, 1, 9, 7, 7], 14))
