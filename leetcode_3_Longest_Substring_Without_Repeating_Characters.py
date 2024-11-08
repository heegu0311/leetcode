# Set Data structure
class Solution1:
    def lengthOfLongestSubstringWithoutRepeatingCharacters(self, s: str) -> int:
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

# Map (Dict) Data structure
class Solution2:
    def lengthOfLongestSubstringWithoutRepeatingCharacters(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charMap = {}
        left = 0
        
        for right in range(n):
            if s[right] not in charMap or charMap[s[right]] < left:
                charMap[s[right]] = right
                maxLength = max(maxLength, right - left + 1)
            else:
                left = charMap[s[right]] + 1
                charMap[s[right]] = right
        
        return maxLength


s1 = Solution1()
s2 = Solution2()

print(s1.lengthOfLongestSubstringWithoutRepeatingCharacters('!@#!@K#!@KD9876!5@4E12!)1232312()SKL123123DA)SDC)ASD(CSAD(C)SADOC)SALDC)!)@_#)!_@#O!@_LD_ASF_SADV(BGBG*D*sdfvoadsCASD_SAD)CAS_DCLSDCDA_SVSADVSA'))
print(s2.lengthOfLongestSubstringWithoutRepeatingCharacters('abcabcbb'))