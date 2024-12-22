class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged = sorted(nums1 + nums2)
        middleIndex = int(len(merged)/2)
        
        if len(merged) % 2 == 0:
            return (merged[middleIndex] + merged[middleIndex - 1]) / 2
        else:
            return merged[middleIndex]
