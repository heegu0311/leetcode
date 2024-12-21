class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest = 1

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        count = 1
        for i, num in enumerate(nums):
            if i < len(nums):
                if nums[i] - nums[i - 1] == 1:
                    count += 1
                elif nums[i] == nums[i - 1]:
                    continue
                else:
                    count = 1

            if count > longest:
                longest = count

        return longest
