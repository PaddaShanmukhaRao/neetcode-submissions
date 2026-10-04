class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0 or len(s)==1:
            return len(s)
        l = 0 
        r = 0 
        res = 0
        charSet = set()
        while l <= r and r < len(s):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res = max(res,r - l + 1)
            r += 1
        return res
