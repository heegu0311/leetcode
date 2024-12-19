class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        charSet = set()
        maxLength = 0
        left = 0
        
        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, len(charSet))
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
        
        return maxLength