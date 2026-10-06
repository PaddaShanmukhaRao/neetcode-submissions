class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # brute itself is so tough
        # res = 0
        # for i in range(len(s)):
        #     count = {}
        #     maxf = 0
        #     for j in range(i,len(s)):
        #         count[s[j]] = 1 + count.get(s[j],0)
        #         maxf = max(maxf,count[s[j]])
        #         if (j - i + 1) - maxf <= k:
        #             res = max(res,(j - i + 1))
        # return res
        i,j = 0,0
        count = {}
        maxf = 0
        res = 0
        while i<=j and j<len(s):
            count[s[j]] = 1 + count.get(s[j],0)
            maxf = max(maxf,count[s[j]])
            if (j-i+1)-maxf <= k:
                res = max((j-i+1),res)
            else:
                count[s[i]]-=1
                i+=1
            j+=1
        return res
            