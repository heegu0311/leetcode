from typing import List, cast
from typing import Optional
        
class Solution1:
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

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_index_dict = {}

        for (i, num) in enumerate(nums):
            complement = target - num
            
            if num in complement_index_dict:
                return [complement_index_dict[num], i]
            else:
                complement_index_dict[complement] = i



s1 = Solution1()
s2 = Solution2()
print(s1.twoSum([11, 2, 7, 15], 9))
print(s2.twoSum([11, 2, 7, 15], 9))
print(s1.twoSum([3, 3], 6))
print(s2.twoSum([3, 3], 6))