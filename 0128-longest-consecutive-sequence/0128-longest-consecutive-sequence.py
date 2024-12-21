class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict = {}
        longest = 1

        if(len(nums) == 0):
            return 0
        if(len(nums) == 1):
            return 1

        for num in nums:
            dict[num] = num + 1
        for num in nums:
            prev = num - 1
            target = dict[num]
            if prev not in dict:
                count = 1
                while target in dict:
                    target += 1
                    count += 1
                longest = max(longest, count)
        return longest
