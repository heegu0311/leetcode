class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l = 0
        r = n - 1

        copy = nums.copy()
        copy.sort()  # sort array for quick search O(n)
        reverseCopy = nums.copy()  # copy array for search O(n)
        reverseCopy.reverse()

        while l < r:
            sumTwo = copy[l] + copy[r]

            if sumTwo == target:
                result = [nums.index(copy[l]), n - 1 - reverseCopy.index(copy[r])]
                result.sort()
                return result

            if sumTwo < target:
                # if(target is greater than sum), move start to the next index
                l += 1
            elif sumTwo > target:
                # if(target is smaller than sum), move start to the prev index
                r -= 1