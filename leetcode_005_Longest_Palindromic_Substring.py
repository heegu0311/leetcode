# Brute force solution (by myself)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        substrings = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
        longest = ''
        for substr in substrings:
            if len(substr) <= len(longest):
                continue
            if self.checkPalindrome(substr) and len(substr) > len(longest):
                longest = substr
        return longest
    
    def checkPalindrome(self, ss: str) -> bool:
        result = True
        for (i, s) in enumerate(ss):
            if i == int(len(ss) / 2):
                return result
            if(s != ss[len(ss) - i - 1]):
                return False
        return result

# solution = Solution()
# print(solution.longestPalindrome('abacdde'))

# two pointer solution

class Solution2:
    def longestPalindrome(self, s: str) -> str:
        longest = ''
        maxLen = 0
        for i in range(len(s)):
            # odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if(r - l + 1 > maxLen): 
                    longest = s[l:r + 1]
                    maxLen = r - l + 1
                r += 1
                l -= 1

            # even
            l,r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if(r - l + 1 > maxLen): 
                    longest = s[l:r + 1]
                    maxLen = r - l + 1
                r += 1
                l -= 1
        return longest
    


solution2 = Solution2()
print(solution2.longestPalindrome('abacdde'))